import os
import random
import string

from flask import Flask
from config import Config


app = Flask(__name__)
app.config.from_object(Config)


def get_random_string():
    randomstring = ''
    alphabet = string.ascii_lowercase+string.ascii_uppercase
    while len(randomstring) <= app.config['RANDOM_NAME_LEN']-1:
        randomstring = randomstring+random.choice(alphabet)
    return randomstring

def get_image_name(image):
    return get_random_string()+'.'+image.filename.rsplit('.', 1)[1].lower()

def image_uploader(image):
    imagename = get_image_name(image)
    image.save(os.path.join(app.config['UPLOADS_FOLDER'], imagename))
    return app.config['APP_URL'] + imagename
