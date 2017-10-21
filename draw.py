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


def draw_text(image, text, font, size, point, collor_code="#FFFFFFFF"):
    collor = ImageColor.getrgb(collor_code)
    if len(collor)==3: collor = tuple(list(collor) + [255])
    
    fnt = ImageFont.truetype('./fonts/%s' % fonts[font], size)
    d = ImageDraw.Draw(image)
    d.text(point, text, font=fnt, fill=collor)
    
    return bg


def draw_lineral(image, json, percent):
    progress = Image.open(BytesIO(decodebytes(json["progress"])))
    if json["stand"] is not None:  
        stand = Image.open(BytesIO(decodebytes(json["stand"])))
    else:
        stand = None
    
    pb = draw_progress(progress, stand, percent, json["border"])
    pb = pb.resize((pb.size[0]*json["w"], pb.size[1]*json["h"]))

    pb = rotate_image(pb, json["angle"])
    image = paste_image(pb, image, (json["x"], json["y"]))
    
    return image

def draw_textview(image, json, percent, current_sum, total):
    text = json["text"].replace("{{total}}", str(total))
    text = text.replace("{{current}}", str(current_sum))
    text = text.replace("{{percent}}", str(percent))
    
    image = draw_text(image, text, json["font"], json["size"], (json["x"], json["y"]), collor_code=json["collor"])
    
    return image


def draw_head(json, current_sum):
    image = Image.open(BytesIO(decodebytes(json["background"])))
    total = json["total"]
    if current_sum == 0: total = 1
    
    percent = int(current_sum/total*100)
    for view in json["views"]:
        if view["type"] == "lineral":
            image = draw_lineral(image, view, percent)
    
    for view in json["views"]:
        if view["type"] == "text":
            image = draw_textview(image, view, percent, current_sum, json["total"])
    
    return image