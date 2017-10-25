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
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __repr__(self):
        return self.name


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    pianos = relationship("Piano", backref="user")

    def __repr__(self):
        return self.email


class Piano(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    title = db.Column(db.String(120), nullable=False)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    bio = db.Column(db.Text)
    update_date = db.Column(db.DateTime, server_default=None)
    image = db.Column(db.String(120), nullable=True)
    url = db.Column(db.String(120), nullable=True)
    active = db.Column(db.Boolean, default=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))




    def __repr__(self):
        return '{} @ ({}, {})'.format(self.title, self.lat,self.lon)




