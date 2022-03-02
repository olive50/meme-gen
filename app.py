import random
import os
import requests
from flask import Flask, render_template, abort, request

# @TODO Import your Ingestor and MemeEngine classes

from Ingestors import  Ingestor
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ charges images  and quotes """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # TODO: Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []
    imgs = []
    images_path = "./_data/photos/dog/"

    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    
    for file in quote_files:
        try:
            quotes.extend(Ingestor.parse(file))
        except ValueError as err:
            print(f"Error when parsing quotes from the file - {file} : {err}")

    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme from random image and quote """

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array
    img = random.choice(imgs)
    quote = random.choice(quotes)
        
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ a form for user data """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    if not request.form["image_url"]:
        return render_template('meme_form.html')

    image_url = request.form["image_url"]
    try:
        r = requests.get(image_url, verify=False)
        tmp = f'./tmp/{random.randint(1,77777)}.png'
        img = open(tmp, 'wb').write(r.content)

    except:
        print("Check the image URL that yougive")
        return render_template('meme_form.html')

    body = request.form["body"]
    author = request.form["author"]
    path = meme.make_meme(tmp, body, author)

    os.remove(tmp)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
