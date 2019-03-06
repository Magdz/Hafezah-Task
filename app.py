from . import app

from controllers import HelloController

@app.route('/')
def hello_world():
    controller = HelloController();
    return controller.hello_world()