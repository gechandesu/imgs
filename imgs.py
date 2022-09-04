__version__ = '1.2'

import os
import random
import string

from bottle import default_app as app
from bottle import run, get, post, request, response, error, template, static_file


config = app().config.load_config('./imgs.ini')

def generate_media_name(media: str) -> str:
    name = ''
    chars = string.ascii_letters + string.digits + '-_'
    while len(name) <= int(config['imgs.file_name_lenght']) - 1:
        name = name + random.choice(chars)
    return name + os.path.splitext(media)[1].lower()

def get_base_url():
    try:
        base_url = config['imgs.base_url']
    except KeyError:
        base_url = request.url
    return base_url

def get_media_url(media_name: str) -> str:
    media_url = get_base_url() + '/' + media_name
    return media_url.replace('//', '/').replace(':/', '://')

def upload_file(file):
    media_name = generate_media_name(file.filename)
    file.save(os.path.join(config['imgs.uploads_dir'], media_name))
    return media_name

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
def upload_media():
    # Handle request from CLI
    if request.files.get('file'):
        file = request.files.get('file')
        rq = 'cli'
    # Handle request from web-browser
    elif request.files.get('media_web'):
        file = request.files.get('media_web')
        rq = 'web'

    if config['imgs.allowed_mime_types'] == '*':
        # Skip MIME checking.
        media_name = upload_file(file)
    else:
        if file.content_type in config['imgs.allowed_mime_types']:
            # Upload file!
            media_name = upload_file(file)
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
                    base_url = get_base_url(), media_url = 'None')
    # Return 200 OK
    if rq == 'cli':
        return get_media_url(media_name) + '\n'
    else:
        return template('index.tpl',
            uploaded = True, not_found = False, bad_mime_type = False,
            media_type = file.content_type.split('/')[0],
            base_url = get_base_url(), media_url = get_media_url(media_name))

@get('/<media_name>')
def send_media(media_name):
    return static_file(media_name, root = config['imgs.uploads_dir'])

@get('/style.css')
def send_style():
    return static_file('style.css', root = './')

@get('/imgs.js')
def send_script():
    return static_file('imgs.js', root = './')

@get('/favicon.ico')
def send_favicon():
    return static_file('favicon.ico', root = './')

app = app()  # Create WSGI application

if __name__ == '__main__':
    run()
