
# lab 10: some fun with PIL 'python image library'
# https://python-pillow.org/

from PIL import Image, ImageDraw
from random import randint

# a useful function for drawing a circle by specifying its center and radius
def draw_circle(x, y, radius, color, draw):
    draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=color)

img_width = 2000
img_height = 2000
img = Image.new('RGB', (img_width, img_height), (255, 255, 255)) #initialize to white
draw = ImageDraw.Draw(img)

print('this might take a moment...')
for i in range(100000):
    x1 = randint(0, img_width)
    y1 = randint(0, img_height)
    x2 = randint(0, img_width)
    y2 = randint(0, img_height)
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    line_width = randint(1, 50)
    draw.line((x1, y1, x2, y2), fill=(red, green, blue), width=line_width)

img.save('temp.jpg')
img.show()




