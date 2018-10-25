
class Config(object):
    DEBUG = True
    SECRET_KEY = 'ourlitlesecret'

class Development(Config):
    Debug = True

class Testing(Config):
    TESTING = True
    Debug = True

app_config = {
    'development' : Development,
    'testing' : Testing
}

