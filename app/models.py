from . import db

class PropertyInfo(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    numberOfBedrooms = db.Column(db.Integer)
    numberOfBathrooms = db.Column(db.Integer)
    location = db.Column(db.String(100))
    price = db.Column(db.Integer)
    ptype = db.Column(db.String(80))
    description = db.Column(db.String(300))
    photoFilename = db.Column(db.String(80))

    def __init__(self, title, numberOfBedrooms, numberOfBathrooms, 
                    location, price, ptype, description, photoFilename
                ):
        self.title = title
        self.numberOfBedrooms = numberOfBedrooms
        self.numberOfBathrooms = numberOfBathrooms
        self.location = location
        self.price = price
        self.ptype = ptype
        self.description = description

    def __repr__(self):
        return '<Property Title: %r>' % self.title

