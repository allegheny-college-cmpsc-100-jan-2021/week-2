from PIL import Image, ImageDraw, ImageFont

def prepare_text(text, align, size):
    
    # load typeface
    face = "type/space-mono.ttf"
    
    # Create font from te type given a size
    font = ImageFont.truetype(face, size)
    
    # Get the picture dimension
    # Access picture via "global" scope
    pic_w, pic_h = picture.size
    type_w, type_h = draw.textsize(text, font=font)
    
    if align == "center":
        point = (
            (pic_w - type_w) / 2, # center the element horizontally
            (pic_h - type_h) / 2  # center the element vertically
        )
    elif align == "right-bottom":
        point = (
            pic_w - type_w - 50, # calculate where in the x dim
            pic_h - type_h - 50  # calculate where in the y dim
        )
    
    return point, font

def apply_text(text, origin, font):
    
    # Use the draw object ("global" scope)
    draw.text(
        (
            origin
        ),
        text,
        fill=(255,153,255),
        font=font
    )

# Open source
poem = open("poems/gomringer_poem.txt","r")
lines = poem.read()

# Canvas
picture = Image.new("RGB",(1024,768))

# Create a draw object
draw = ImageDraw.Draw(picture)

# Determine how to write/space textual element
pos, font = prepare_text(lines,"center",48)

# get the text into the image
apply_text(lines, pos, font)

attr = "Silence\nEugen Gomringer"

# Reuse the placement, preparation function
pos, font = prepare_text(attr,"right-bottom",30)

# Reuse the apply function
apply_text(attr, pos, font)

# Save picture step
picture.save("gomringer_poem.png")