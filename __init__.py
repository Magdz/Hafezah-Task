import os
import boto3
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_googlemaps import GoogleMaps
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

app = Flask(__name__, template_folder=".")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['GOOGLEMAPS_KEY'] = os.getenv('GOOGLEMAPS_KEY')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
GoogleMaps(app)

from .models import *

db.create_all()

s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    
