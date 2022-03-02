"""This class is used to generate memes."""

import os
import random

from PIL import Image, ImageFont, ImageDraw


class MemeEngine:
    """The Class tha generate a meme."""

    def __init__(self, output_dir):
        """Instantiate objects."""
        self.output_dir = output_dir
        self.count = 1
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def make_meme(self, img_path, text, author, width=500):
        """Generate a mem.

        Arguments:
        img_path -- the path to the file.
        text -- the body of the quote.
        author -- the author of this quote.
        width -- the widht of the image.

        return :
        a path to the generated meme(image with text).
        """
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
