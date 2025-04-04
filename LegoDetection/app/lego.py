from app import db

class LegoPiece(db.Model):
    __tablename__ = 'piece'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    color = db.Column(db.String)
    brickid = db.Column(db.String)
    quantity = db.Column(db.Integer)

    def __init__(self, name, color, brickid, quantity):
        self.name = name
        self.color = color
        self.brickid = brickid
        self.quantity = quantity