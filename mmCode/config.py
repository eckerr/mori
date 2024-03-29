# config.py  for Mori Flask app
import os
class Configuration(object):
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/mori.db' % APPLICATION_DIR
    STATIC_DIR = os.path.join(APPLICATION_DIR, 'static')
    IMAGES_DIR = os.path.join(STATIC_DIR, 'images')

    SECRET_KEY = 'Mori is something special' # Unique key for this app

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DEBUG = True
