# 1: import the appropriate libraries
from PIL import Image, ImageDraw
import random

# 2: Create a canvas of correct size
painting = Image.new(
    'RGB',
    (1920,1080),
    (140,150,77)
)

# 3: On that canvas, place at least one of:
#       - circle
#       - square
#       - polygon of your choice (triangle, others)
draw = ImageDraw.Draw(painting)

#rather than generating random colors multiple times, possible to simply assign it to a variable
def random_color_scale ():
    rcs = random.randint(0, 255)
    return rcs

def pos_gen(x,y):
    random_pos = random.randint(x,y)
    return random_pos

draw.rectangle(
    #The random assignments will change the locations of the shapes each time within their respective ranges
    (
        (pos_gen(45,129), pos_gen(80,220)),
        (pos_gen(300, 350), pos_gen(400, 600))
    ),
    fill=(
        random_color_scale(), 
        130, 
        random_color_scale()
    )
)