class Config(object):
    DEBUG = True
    APP_URL = 'http://127.0.0.1:5000/' # "/" in end is important!
    UPLOADS_FOLDER = '/mnt/develop/imgs/imgs/uploads/'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024 # Value in bytes. There is 16M.
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp', 'gif'} # Not yet implemented.
    RANDOM_NAME_LEN = 5
