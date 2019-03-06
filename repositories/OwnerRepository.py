from .. import db
from ..models import Owner

class OwnerRepository:
    def __init__(self):
        pass

    def find(self, username):
        return Owner.query.filter_by(username=username).first_or_404()