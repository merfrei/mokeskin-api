import os


DEFAULT_ENVIRON = 'dev'


DEFAULT_CONFIG = {
    'API_URL': '/api/v1.0/',
    'DEBUG': False,
    'TESTING': False,
    'DATABASE_URI': 'redis://localhost:6798',
    'DATABASE_POOL_MIN': 5,
    'DATABASE_POOL_MAX': 25,
    'API_KEY': 'phahg3EiB@i2Wi!Z'
}


PRODUCTION = DEFAULT_CONFIG.copy()

DEVELOPMENT = DEFAULT_CONFIG.copy()
DEVELOPMENT['DEBUG'] = True

TESTING = DEFAULT_CONFIG.copy()
TESTING['TESTING'] = True
TESTING['DATABASE_URI'] = 'redis://localhost:6799'


CONFIG = {
    'dev': DEVELOPMENT,
    'test': TESTING,
    'prod': PRODUCTION,
}


def get_config():
    environ = DEFAULT_ENVIRON
    if 'API_ENVIRON' in os.environ:
        environ = os.environ['API_ENVIRON']
    return CONFIG[environ]
