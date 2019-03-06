from .. import db
from ..models import Restaurant

class RestaurantRepository:
    def __init__(self):
        pass

    def all(self):
        return Restaurant.query.all()

    def find_by_owner(self, ownerId):
        return Restaurant.query.filter_by(owner_id=ownerId).first()

    def update(self, restaurant, data):
        if 'name' in data:
            restaurant.name = data['name']
        if 'phoneNumber' in data:
            restaurant.phone_number = data['phoneNumber']
        if 'longitude' in data:
            restaurant.longitude = data['longitude']            
        if 'latitude' in data:
            restaurant.latitude = data['latitude']
            
        db.session.commit()
        return restaurant