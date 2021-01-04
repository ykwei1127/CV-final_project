from PIL import Image
import numpy as np

def merge(background, portrait, scale=1):
    width1, height1 = background.size
    width2, height2 = portrait.size

    if scale != 1:
        width2 = width2 * scale
        height2 = height2 * scale
        portrait = portrait.resize((width2, height2))

    anchor_x = width1 - width2
    anchor_y = height1 - height2

    for w in range(width2):
        for h in range(height2):
            p = portrait.getpixel((w,h))
            if p != (0,0,0):
                background.putpixel((w+anchor_x-500,h+anchor_y), p)
    background.save('result.png')


if __name__ == '__main__':
    background = Image.open('lab.jpg')
    portrait = Image.open('portrait.png')
    merge(background, portrait, 2)
