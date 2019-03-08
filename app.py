import json
from flask import request

from . import app
from .controllers import OwnerController, RestaurantController

@app.route('/owner/register', methods=['POST'])
def register_owner():
    controller = OwnerController()
    data = json.loads(request.data)
    return json.dumps(controller.register_owner(data))

@app.route('/owner/auth', methods=['POST'])
def auth_owner():
    controller = OwnerController()
    data = json.loads(request.data)
    return json.dumps(controller.auth_owner(data))

@app.route('/restaurants/nearby', methods=['POST'])
def nearby_restaurants():
    controller = RestaurantController()
    data = json.loads(request.data)
    return json.dumps(controller.nearby_restaurants(data))

@app.route('/restaurants', methods=['POST', 'PATCH'])
def crud_restaurant():
    controller = RestaurantController()
    data = json.loads(request.data)
    token = request.headers.get('Authorization')

    if request.method == 'POST':
        return json.dumps(controller.create_restaurant(token, data))
    if request.method == 'PATCH':
        return json.dumps(controller.edit_restaurant(token, data))
    return json.dumps({})

@app.route('/restaurants/logo/upload', methods=['POST'])
def upload_logo():
    controller = RestaurantController()
    logo = request.files['logo']
    token = request.headers.get('Authorization')
    return json.dumps(controller.upload_logo(token, logo))
