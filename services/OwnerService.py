from .. import bcrypt
from ..repositories import OwnerRepository

class OwnerService:
    def auth(self, credentials):
        repository = OwnerRepository()
        owner = repository.find(credentials["username"])
        authenticated = bcrypt.check_password_hash(owner.password, credentials["password"])
        if not authenticated:
            return None
        return owner 
    