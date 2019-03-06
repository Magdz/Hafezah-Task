from . import app

from controllers import HelloController

@app.route('/')
def hello_world():
    print app
    controller = HelloController(app);
    return controller.hello_world()