import os
from math import sin, cos, sqrt, atan2, radians

from .. import s3
from ..repositories import RestaurantRepository

class RestaurantService:
    def update(self, ownerId, data):
        repository = RestaurantRepository()
        restaurant = repository.find_by_owner(ownerId)
        restaurant = repository.update(restaurant, data)
        return restaurant

    def upload_logo(self, ownerId, logo):
        repository = RestaurantRepository()
        restaurant = repository.find_by_owner(ownerId)

        data = {}
        try:
            bucket_name = os.getenv('S3_BUCKET')
            s3.upload_fileobj(
                logo,
                bucket_name,
                logo.filename,
                ExtraArgs={
                    "ACL": "public-read",
                    "ContentType": logo.content_type
                }
            )
            data['logo'] = 'http://{}.s3.amazonaws.com/{}'.format(bucket_name, logo.filename)
        except Exception as e:
            print(e)
            
        repository.update(restaurant, data)
        return restaurant

    def list_nearby(self, data):
        repository = RestaurantRepository()
        all_restaurants = repository.all()
        nearby_restaurants = self.__filter_nearby(data, all_restaurants)
        return nearby_restaurants

    def __filter_nearby(self, data, restaurants):
        output = {}
        walkable_distance = 1

        radius = 6373.0
        person_lat = radians(data["latitude"])
        person_lng = radians(data["longitude"])

        for restaurant in restaurants:
            restaurant_lat = radians(restaurant.latitude)
            restaurant_lng = radians(restaurant.longitude)

            lat_diff = restaurant_lat - person_lat
            lng_diff = restaurant_lng - person_lng

            a = sin(lat_diff / 2)**2 + cos(person_lat) * cos(restaurant_lat) * sin(lng_diff / 2)**2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))

            distance = radius * c
            if (distance <= walkable_distance):
                output[distance] = (restaurant)

        return output.values()
        