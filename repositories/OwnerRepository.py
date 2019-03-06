from .. import db
from ..models import Owner

class OwnerRepository:
    def __init__(self):
        pass

    def all(self):
        return Owner.query.all()