from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
# from dotenv import load_dotenv, find_dotenv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/hafezah'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

import models

db.create_all()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    
