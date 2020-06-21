from flask import Flask
from config import Config
import random, os

app = Flask(__name__)
app.config.from_object(Config)

def GetRandomName():
    randomstring=''
    while len(randomstring)<=app.config['RANDOM_NAME_LEN']-1:
        randomstring = randomstring+random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return randomstring

def GetImageName(imageObj):
    return GetRandomName()+'.'+imageObj.filename.rsplit('.', 1)[1].lower()

# def GetImage(imageName):
    # return send_from_directory(app.config['UPLOADS_FOLDER'], imageName)

