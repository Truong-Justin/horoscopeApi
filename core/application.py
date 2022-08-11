from flask import Flask
from decouple import config
from flask_restx import Api


#Flask object made called app
application = Flask(__name__)
application.config.from_object(config("APP_SETTINGS"))


#Api object is made named api
api = Api(
    application,
    version='1.0',
    title='Horoscope API',
    description='Get horoscope data using the below APIs',
    license='MIT',
    contact='Justin Truong',
    contact_email='truongj1951@uhcl.edu',
    doc='/',
    prefix='/api'
)

from core import routes
