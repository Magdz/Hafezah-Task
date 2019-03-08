from .. import db
from ..models import Owner

class OwnerRepository:
    def create(self, data):
        owner = Owner(email=data['email'], username=data['username'], password=data['password'])
        db.session.add(owner)
        db.session.commit()
        return owner

    def find(self, username):
        return Owner.query.filter_by(username=username).first_or_404()