from .. import db

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(225), nullable=False)
    logo = db.Column(db.String(225), nullable=True)
    phone_number = db.Column(db.String(20), nullable=True)
    longitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'), unique=True, nullable=False)

    def __repr__(self):
        return '<Restaurant %r>' % self.name