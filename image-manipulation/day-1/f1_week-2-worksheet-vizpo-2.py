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
        fill='yellow',             # <-- color of text
        font=font                 # <-- font object to use when writing
    )

# TODO: Using our other example as a model, complete this small project
#       by opening the file located at poems/saroyan_poem.txt and
#       create an image of it; the author and title are located in the
#       worksheet.