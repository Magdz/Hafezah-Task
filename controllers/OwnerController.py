import os
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

        token = jwt.encode({"ownerId": owner.id}, os.getenv('JWT_SECRET'), algorithm=os.getenv('JWT_ALGORITHM'))
        return {
            "token": 'Bearer ' + token 
        }
