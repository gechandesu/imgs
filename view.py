import os
from flask import render_template, request, url_for, send_from_directory
from imgs import app, get_image_name, image_uploader


@app.route('/', methods = ['GET'])
def index_page():
    return render_template('index.html')

@app.route('/', methods = ['POST'])
def uploader():
    if request.files:
        if "image" in request.files:  # For uploads via curl -F
            output = image_uploader(request.files["image"])
            return output + '\n'
        elif "image_web" in request.files:  # For uploads via web interface
            output = image_uploader(request.files["image_web"])
            return render_template('index.html', image_url = output, uploaded = True)

@app.route('/<imagename>')
def getimage(imagename):
    return send_from_directory(app.config['UPLOADS_FOLDER'], imagename)

@app.route('/about')
def about_page():
    return render_template('about.html')
