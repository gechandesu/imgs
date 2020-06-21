class Config(object):
    DEBUG = True
    UPLOADS_FOLDER = '/mnt/develop/imgs/imgs/uploads/'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp', 'gif'} # Не реализован
    RANDOM_NAME_LEN = 5
