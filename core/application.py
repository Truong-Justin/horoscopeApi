from flask import Flask
from decouple import config
from flask_restx import Api


#Flask object made called app
app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))


#Api object is made named api
api = Api(
    app,
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
