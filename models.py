from sqlalchemy.orm import relationship, backref
from sqlalchemy import Boolean, DateTime, Column, Integer, \
                       String, ForeignKey
from flask_security import UserMixin, RoleMixin

from app import db, bcrypt

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return self.name

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(120))
    city = db.Column(db.String(120))
    active = db.Column(db.Boolean(), default=True)
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    pianos = relationship("Piano", backref="user")

    def __repr__(self):
        return self.email


class Piano(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lon = db.Column(db.Float, nullable=False)
    bio = db.Column(db.Text)
    update_date = db.Column(db.DateTime, server_default=None)
    url = db.Column(db.String(120))
    active = db.Column(db.Boolean, default=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    image = relationship("Image", uselist=False, backref="piano")

    def __repr__(self):
        return '{} @ ({}, {})'.format(self.title, self.lat,self.lon)

    def json_dump(self):
        pianoJson = {}
        pianoJson['lat'] = self.lat
        pianoJson['lon'] = self.lon
        pianoJson['image'] = str(self.image)
        pianoJson['title'] = self.title
        pianoJson['bio'] = self.bio
        pianoJson['url'] = self.url

        return pianoJson

      
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    path = db.Column(db.String(128))
    piano_id = db.Column(db.Integer, ForeignKey('piano.id'))
    
    def __repr__(self):
        return self.path



