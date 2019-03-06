from ..repositories import RestaurantRepository

class RestaurantService:
    def __init__(self):
        pass

    def list_nearby(self, data):
        repository = RestaurantRepository()
        restaurants = repository.all()

        return restaurants