from flask import Flask, request
from dotenv import load_dotenv, find_dotenv

from controllers import HelloController

app = Flask(__name__)

@app.route('/')
def hello_world():
    return HelloController.hello_world()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    