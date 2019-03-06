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

    def edit_restaurant(self, token, data):
        payload = jwt.decode(token.replace('Bearer ', ''), 'secret', algorithms=['HS256'])
        service = RestaurantService()
        restaurant = service.update(payload['ownerId'], data)
        return self.__mapper(restaurant)

    def __mapper(self, restaurant):
        return {
            "id": restaurant.id,
            "name": restaurant.name,
            "phoneNumber": restaurant.phone_number,
            "longitude": restaurant.longitude,
            "latitude": restaurant.latitude
        }
