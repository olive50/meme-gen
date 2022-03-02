
"""This module gives the possiblite to creat a meme based on an image and a quote."""
import os
import random

from PIL import Image, ImageFont, ImageDraw

class MemeEngine:
    """"""
    def __init__(self, output_dir):
        self.output_dir = output_dir
        self.count = 1
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def make_meme(self, img_path, text, author, width=500):
        """ generate meme for using image and a quote(text and author)."""
        img = Image.open(img_path)
        outfile = os.path.join(self.output_dir, f"temp-{self.count}.jpg")
        self.count += 1
        real_width, real_height = img.size
        height = int(real_height * width / real_width)
        img.thumbnail((width, height))

        font1 = ImageFont.truetype("./_data/Fonts/LilitaOne-Regular.ttf", 24)
        font2 = ImageFont.truetype("./_data/Fonts/LilitaOne-Regular.ttf", 16)
        text_position = random.choice(range(20, height - 40))
        fill = (0, 0, 0)
        stroke_fill = (255, 255, 255)
        draw = ImageDraw.Draw(img)
        draw.text((30, text_position), text, fill, font1,
                  stroke_width=1, stroke_fill=stroke_fill)
        draw.text((40, text_position + 25), f"- {author}", fill, font2,
                  stroke_width=1, stroke_fill=stroke_fill)

        img.save(outfile, "JPEG")
        return outfile
