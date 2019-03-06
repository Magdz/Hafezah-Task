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

@app.route('/restaurants', methods=['PATCH'])
def edit_restaurant():
    controller = RestaurantController()
    data = json.loads(request.data)
    token = request.headers.get('Authorization')
    return json.dumps(controller.edit_restaurant(token, data))

@app.route('/restaurants/logo/upload', methods=['POST'])
def upload_logo():
    controller = RestaurantController()
    logo = request.files['logo']
    token = request.headers.get('Authorization')
    return json.dumps(controller.upload_logo(token, logo))
