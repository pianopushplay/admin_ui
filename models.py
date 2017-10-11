from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from app import db, bcrypt

class Piano(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    geolat = db.Column(db.Float, nullable=False)
    geolong = db.Column(db.Float, nullable=False)
    update_date = db.Column(db.DateTime, server_default=None)
    is_active = db.Column(db.Boolean, default=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    
    def __init__(self, name, geolat, geolong,update_date, admin_id):
        pass

    def img(self, size):
        pass

    def __repr__(self):
        return '{} @ ({}, {})'.format(self.name, self.geolat,self.geolong)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(560))
    is_superuser = db.Column(db.Boolean(), default=False)
    pianos = relationship("Piano", backref="user")

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<name - {}>'.format(self.name)
