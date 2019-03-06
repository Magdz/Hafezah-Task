import json
from flask import request

from . import app

from controllers import OwnerController, RestaurantController

@app.route('/restaurants/nearby', methods=['POST'])
def nearby_restaurants():
    controller = RestaurantController()
    data = json.loads(request.data)
    return json.dumps(controller.nearby_restaurants(data))

@app.route('/owner/auth', methods=['POST'])
def auth_owner():
    controller = OwnerController()
    data = json.loads(request.data)
    return json.dumps(controller.auth_owner(data))