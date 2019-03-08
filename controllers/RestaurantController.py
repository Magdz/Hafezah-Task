import os
import jwt
import json

from ..services import RestaurantService

class RestaurantController:
    def nearby_restaurants(self, data):
        service = RestaurantService()
        restaurants = service.list_nearby(data)
        output = []
        for restaurant in restaurants:
            output.append(self.__mapper(restaurant))
        return output

    def create_restaurant(self, token, data):
        payload = self.__get_payload(token)
        service = RestaurantService()
        restaurant = service.create(payload['ownerId'], data)
        return self.__mapper(restaurant)

    def edit_restaurant(self, token, data):
        payload = self.__get_payload(token)
        service = RestaurantService()
        restaurant = service.update(payload['ownerId'], data)
        return self.__mapper(restaurant)

    def upload_logo(self, token, logo):
        payload = self.__get_payload(token)
        service = RestaurantService()
        restaurant = service.upload_logo(payload['ownerId'], logo)
        return {
            "url": restaurant.logo
        }

    def __mapper(self, restaurant):
        return {
            "id": restaurant.id,
            "name": restaurant.name,
            "logo": restaurant.logo,
            "phoneNumber": restaurant.phone_number,
            "longitude": restaurant.longitude,
            "latitude": restaurant.latitude
        }

    def __get_payload(self, token):
        return jwt.decode(token.replace('Bearer ', ''), os.getenv('JWT_SECRET'), algorithms=[os.getenv('JWT_ALGORITHM')])
        
