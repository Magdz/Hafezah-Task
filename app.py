import json
from flask import request

from . import app

from controllers import HelloController, RestaurantController

@app.route('/')
def hello_world():
    controller = HelloController()
    return controller.hello_world()

@app.route('/restaurants/nearby', methods=['POST'])
def nearby_restaurants():
    controller = RestaurantController()
    data = json.loads(request.data)
    return json.dumps(controller.nearby_restaurants(data))