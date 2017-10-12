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
    # confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    pianos = relationship("Piano", backref="user")

    # def __init__(self, name, email, password):
    #     self.name = name
    #     self.email = email
    #     self.password = bcrypt.generate_password_hash(password)

    def __repr__(self):
        return self.email


class Piano(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    geolat = db.Column(db.Float, nullable=False)
    geolong = db.Column(db.Float, nullable=False)
    update_date = db.Column(db.DateTime, server_default=None)
    is_active = db.Column(db.Boolean, default=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))

    # def __init__(self, name, geolat, geolong,update_date):
    #     pass

    def img(self, size):
        pass

    def __repr__(self):
        return '{} @ ({}, {})'.format(self.name, self.geolat,self.geolong)





