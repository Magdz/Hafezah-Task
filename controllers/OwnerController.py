import jwt
import json

from ..services import OwnerService

class OwnerController:
    def auth_owner(self, credentials):
        service = OwnerService()
        owner = service.auth(credentials)
        if not owner:
            return {
                "error": "Unauthenticated"
            }

        encoded_jwt = jwt.encode({"ownerId": owner.id}, 'secret', algorithm='HS256')
        return {
            "token": 'Bearer ' + encoded_jwt 
        }
