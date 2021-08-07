import os
import random
import string

from bottle import default_app as app
from bottle import run, get, post, request, response, error, template, static_file


config = app().config.load_config('./imgs.ini')

def generate_image_name(image: str) -> str:
    name = ''
    chars = string.ascii_letters + string.digits + '-_'
    while len(name) <= int(config['imgs.image_name_lenght']) - 1:
        name = name + random.choice(chars)
    return name + os.path.splitext(image)[1].lower()

def get_base_url():
    try:
        base_url = config['imgs.base_url']
    except KeyError:
        base_url = request.url
    return base_url

def get_image_url(image_name: str) -> str:
    image_url = get_base_url() + '/' + image_name
    return image_url.replace('//', '/').replace(':/', '://')

def upload_file(file):
    image_name = generate_image_name(file.filename)
    file.save(os.path.join(config['imgs.uploads_dir'], image_name))
    return image_name

@error(404)
def error404(error):
    return template('index.tpl',
        uploaded = False, not_found = True, bad_mime_type = False,
        base_url = get_base_url())

@get('/')
def index():
    return template('index.tpl',
        uploaded = False, not_found = False, bad_mime_type = False,
        base_url = get_base_url())

@post('/')
def upload_image():
    # Handle request from CLI
    if request.files.get('image'):
        file = request.files.get('image')
        if file.content_type in config['imgs.allowed_mime_types']:
            image_name = upload_file(file)
            return get_image_url(image_name) + '\n'
        else:
            # Prevent recource leek. Force close buffered file
            request.body.close()
            response.status = 415
            return 'Error: bad file MIME type\n'
    # Handle request from web-browser
    elif request.files.get('image_web'):
        file = request.files.get('image_web')
        if file.content_type in config['imgs.allowed_mime_types']:
            image_name = upload_file(file)
            return template('index.tpl',
                uploaded = True, not_found = False, bad_mime_type = False,
                base_url = get_base_url(), image_url = get_image_url(image_name))
        else:
            # Prevent recource leek. Force close buffered file
            request.body.close()
            response.status = 415
            return template('index.tpl',
                uploaded = False, not_found = False, bad_mime_type = True,
                allowed_mime_types = config['imgs.allowed_mime_types'],
                base_url = get_base_url(), image_url = 'None')

@get('/<image_name>')
def send_image(image_name):
    return static_file(image_name, root = config['imgs.uploads_dir'])

@get('/style.css')
def send_style():
    return static_file('style.css', root = './')

if __name__ == '__main__':
    run(debug = config['imgs.debug'])
