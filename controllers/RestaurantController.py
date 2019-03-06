import json

from ..services import RestaurantService

class RestaurantController:
    def nearby_restaurants(self, data):
        service = RestaurantService()
        restaurants = service.list_nearby(data)
        output = []
        for restaurant in restaurants:
            output.append({
                "id": restaurant.id
            })
        return output
