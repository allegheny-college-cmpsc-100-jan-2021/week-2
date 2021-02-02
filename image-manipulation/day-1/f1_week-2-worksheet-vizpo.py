# Import required libraries
from PIL import Image, ImageDraw, ImageFont

def prepare_text(text, align, size):
    
    # Setup typeface details/path
    face = 'type/space-mono.ttf'
    
    # Create font from type at a given size
    font = ImageFont.truetype(face,size)
    
    # Get picture dimensions
    pic_w, pic_h = picture.size
    type_w, type_h = draw.textsize(text, font=font)
    
    if align == "center":
        point = (
            (pic_w - type_w) / 2, # <-- center text horizontally
            (pic_h - type_h) / 2  # <-- center text vertically
        )
    elif align == "right-bottom":
        point = (
            pic_w - type_w - 50,  # <-- calculate "x" boundary, give 50 px barrier
            pic_h - type_h - 50   # <-- calculate "y" boundary, give 50 px barrier
        )
    
    return point, font

def apply_text(text, origin, font):

    # Use draw object to apply text
    draw.text(
        (
            origin
        ),
        text,                     # <-- source text to write
        fill='white',             # <-- color of text
        font=font                 # <-- font object to use when writing
    )

# Open source file
poem = open("poems/gomringer_poem.txt","r")
lines = poem.read()

# Create image to write to
picture = Image.new("RGB",(1024,768))

# Set up ability to draw on the picture
draw = ImageDraw.Draw(picture)

# Center poem text
pos, font = prepare_text(lines, "center", 30)

# Write poem text to image
apply_text(lines, pos, font)

# Provide attribution text with newline character
attr = '"Silence"\nEugen Gomringer'

# Right-bottom justify attribution
pos, font = prepare_text(attr, "right-bottom", 20)

# Write attribution to image
apply_text(attr, pos, font)

# Save picture
picture.save("gomringer_poem.png")