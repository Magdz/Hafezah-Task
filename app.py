import json
from flask import request

from . import app

from controllers import RestaurantController

@app.route('/restaurants/nearby', methods=['POST'])
def nearby_restaurants():
    controller = RestaurantController()
    data = json.loads(request.data)
    return json.dumps(controller.nearby_restaurants(data))