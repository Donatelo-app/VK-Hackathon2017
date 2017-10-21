from PIL import Image, ImageDraw, ImageFont, ImageColor
from base64 import encodebytes, decodebytes
from io import BytesIO


fonts = {
    "BEBAS": "Bebas-Regular.ttf",
    "ROBOTO": "Roboto-Regular.ttf"
}


def rotate_image(image, angel):
    max_s = int((image.size[0]**2+image.size[1]**2)**0.5)
    canvas = Image.new("RGBA", (max_s, max_s))
    canvas.paste(image, (max_s//2-image.size[0]//2, max_s//2-image.size[1]//2))
    
    return canvas.rotate(angel)


def paste_image(image, background, point):
    point = point[0]- image.size[0]//2, point[1]- image.size[1]//2
    
    background.paste(image, point, image)
    
    return background


def draw_progress(progress, stand, precent, border):
    if stand is None: stand = Image.new("RGBA", progress.size)
    
    progress = progress.crop((0,0,progress.size[0]/100*precent, progress.size[1]))
    stand = stand.resize((stand.size[0]+border*2, stand.size[1]+border*2))
    try:
        stand.paste(progress, (border, border), progress)
    except:
        stand.paste(progress, (border, border))
    return stand


def draw_text(image, text, font, size, point, color_code="#FFFFFFFF"):
    color = ImageColor.getrgb(color_code)
    if len(color)==3: color = tuple(list(color) + [255])
    
    fnt = ImageFont.truetype('./fonts/%s' % fonts[font], size)
    d = ImageDraw.Draw(image)
    d.text(point, text, font=fnt, fill=color)
    
    return image


def draw_lineral(image, json, percent):
    progress = Image.open(BytesIO(decodebytes(json["progress"].encode())))
    if json["stand"] is not None:  
        stand = Image.open(BytesIO(decodebytes(json["stand"].encode())))
    else:
        stand = None
    
    pb = draw_progress(progress, stand, percent, json["border"])
    pb = pb.resize((json["w"], json["h"]))

    pb = rotate_image(pb, json["angle"])
    image = paste_image(pb, image, (json["x"], json["y"]))
    
    return image

def draw_textview(image, json, percent, current_sum, total):
    text = json["text"].replace("{{total}}", str(total))
    text = text.replace("{{current}}", str(current_sum))
    text = text.replace("{{percent}}", str(percent))
    
    image = draw_text(image, text, json["font"], json["size"], (json["x"], json["y"]), color_code=json["color"])
    
    return image


def draw_cover(json, current_sum):
    image = Image.open(BytesIO(decodebytes(json["background"].encode())))
    total = json["total"]
    if current_sum == 0: total = 1
    
    percent = int(current_sum/total*100)
    for view in json["views"]:
        try:
            if view["type"] == "lineral":
                image = draw_lineral(image, view, percent)
        except TypeError:
            continue
    
    for view in json["views"]:
        try:
            if view["type"] == "text":
                image = draw_textview(image, view, percent, current_sum, json["total"])
        except TypeError:
            continue
    
    return image