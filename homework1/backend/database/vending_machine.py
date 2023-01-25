from app_init import db


class VendingMachine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)

    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __repr__(self):
        return '<VendingMachine %r>' % self.name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location
        }
