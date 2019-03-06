from .. import db
from ..models import Restaurant

class RestaurantRepository:
    def __init__(self):
        pass

    def all(self):
        return Restaurant.query.all()