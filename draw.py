from PIL import Image, ImageDraw, ImageFont, ImageColor


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