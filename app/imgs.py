__version__ = '1.2'

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

def upload_file(file, use_original_name: bool = False, overwrite_existing: bool = False):
    image_name = file.filename if use_original_name else generate_image_name(file.filename)

    if use_original_name and not overwrite_existing:
        base_name, extension = os.path.splitext(image_name)
        counter = 1
        while os.path.exists(os.path.join(config['imgs.uploads_dir'], image_name)):
            image_name = f"{base_name}_{counter}{extension}"
            counter += 1
    elif not use_original_name:
        while os.path.exists(os.path.join(config['imgs.uploads_dir'], image_name)):
            image_name = generate_image_name(file.filename)

    file.save(os.path.join(config['imgs.uploads_dir'], image_name),overwrite=True)
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
    use_original_name = request.forms.get('use_original_name') == 'on'
    overwrite_existing = request.forms.get('overwrite_existing') == 'on'
    if request.files.get('image'):
        file = request.files.get('image')
        rq = 'cli'
    # Handle request from web-browser
    elif request.files.get('image_web'):
        file = request.files.get('image_web')
        rq = 'web'

    if config['imgs.allowed_mime_types'] == '*':
        # Skip MIME checking.
        image_name = upload_file(file,use_original_name, overwrite_existing)
    else:
        if file.content_type in config['imgs.allowed_mime_types']:
            # Upload file!
            image_name = upload_file(file,use_original_name, overwrite_existing)
        else:
            # Show MIME type error!
            # Prevent recource leek. Force close buffered file
            request.body.close()
            response.status = 415
            if rq == 'cli':
                return 'Error: bad file MIME type\n'
            else:
                return template('index.tpl',
                    uploaded = False, not_found = False, bad_mime_type = True,
                    allowed_mime_types = config['imgs.allowed_mime_types'],
                    base_url = get_base_url(), image_url = 'None')
    # Return 200 OK
    if rq == 'cli':
        return get_image_url(image_name) + '\n'
    else:
        return template('index.tpl',
            uploaded = True, not_found = False, bad_mime_type = False,
            base_url = get_base_url(), image_url = get_image_url(image_name))

@get('/<image_name>')
def send_image(image_name):
    return static_file(image_name, root = config['imgs.uploads_dir'])

@get('/style.css')
def send_style():
    return static_file('style.css', root = './')

app = app()  # Create WSGI application

if __name__ == '__main__':
    run()
