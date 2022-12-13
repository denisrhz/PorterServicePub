from datetime import datetime
from app import db

from flask_security import UserMixin, RoleMixin

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(64), nullable=False, unique=True)
    title = db.Column(db.String(64), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(256))
    description = db.Column(db.String(256))

    messages = db.relationship('Message', backref='service', lazy='dynamic')

    def __repr__(self):
        return '{}'.format(self.title)

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    active = db.Column(db.Boolean())

    messages = db.relationship('Message', backref='city', lazy='dynamic')

    def __repr__(self):
        return '{}'.format(self.name)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(64), nullable=False)
    phone = db.Column(db.String(11), index=True, nullable=False)
    body = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    service_id = db.Column(db.Integer, db.ForeignKey('service.id'))
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))

    def __repr__(self):
        return '{}: {}'.format(self.author, self.phone)

# Flask Security #
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
    )

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

class Role(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(255))