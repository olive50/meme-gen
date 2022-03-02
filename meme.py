"""Enty point for the app via CLI."""

import os
import random
import argparse

# @TODO Import your Ingestor and MemeEngine classes
from Ingestors import QuoteModel, Ingestor
from MemeEngine.MemeEngine import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """Generate a meme.

    Arguments:
    path -- the path to the image
    body -- the body of the quote
    author -- the author of the quote.
    """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path
    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesCSV.csv',
                       './_data/DogQuotes/DogQuotesPDF.pdf']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Give author for the given quote text')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    # @TODO Use ArgumentParser to parse the following CLI arguments
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image

    parser = argparse.ArgumentParser(description="Meme Generator.")
    parser.add_argument("--path", type=str, help="The image path")
    parser.add_argument("--body", type=str, help="The Text of the citation")
    parser.add_argument("--author", type=str, default="Inknown",
                        help="The author of the quote (citation)")
    args = parser.parse_args()
    path = args.path
    body = args.body
    author = args.author

    print(generate_meme(args.path, args.body, args.author))
