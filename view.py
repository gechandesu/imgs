import os
from config import Config
from imgs import app, GetImageName
from flask import render_template, request, url_for, redirect, send_from_directory, flash

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def uploader():
        if request.files:
            image = request.files['image']
            imagename = GetImageName(image)
            image.save(os.path.join(app.config['UPLOADS_FOLDER'], imagename))
        return render_template('uploaded.html', ImageURL=request.base_url+imagename)

@app.route('/<imagename>')
def getimage(imagename):
    return send_from_directory(app.config['UPLOADS_FOLDER'], imagename)

@app.route('/about')
def aboutpage():
    return render_template('about.html')
