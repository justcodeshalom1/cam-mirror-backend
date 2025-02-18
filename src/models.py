from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), unique=False, nullable=False)
    last_name = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(256), unique=False, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now(), nullable=True)

    def __repr__(self):
        return '<Users %r>' % self.email


    def serialize(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "password": self.password,
            "id": self.id,
            "created_date": self.created_date
        }


class Membership(db.Model):
    __tablename__ = 'membership'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    membership_name = db.Column(db.String(250), unique=False, nullable=False)
    card_holder_name = db.Column(db.String(120), unique=False, nullable=False)
    card_number = db.Column(db.Integer, unique=True, nullable=False)
    card_expiration_date = db.Column(db.Integer, unique=True, nullable=False)
    card_cvv = db.Column(db.Integer, unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Membership %r>' % self.id


    def serialize(self):
        return {
            "id": self.id,
            "membership_name": self.membership_name,
            "card_holder_name": self.card_holder_name,
            "card_number": self.card_number,
            "card_expiration_date": self.card_expiration_date,
            "card_cvv": self.card_cvv,
            "user_id": self.user_id
        }


class Profiles(db.Model):
    __tablename__ = 'profiles'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now(), nullable=True)
    updated_date = db.Column(db.DateTime, nullable=True)
    membership_id = db.Column(db.Integer, db.ForeignKey('membership.id'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


    def __repr__(self):
        return '<Users %r>' % self.id


    def serialize(self):
        return {
            "created_date": self.created_date,
            "updated_date": self.updated_date,
            "membership_id": self.membership_id,
            "id": self.id,
            "user_id": self.user_id
        }


class Pictures(db.Model):
    __tablename__ = 'pictures'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    updated_date = db.Column(db.String(250), nullable=False)
    pic_folder = db.Column(db.String(250), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Pictures %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "updated_date": self.updated_date,
            "date": self.date,
            "pic_folder": self.pic_folder,
            "user_id": self.user_id,
            "url": self.url
        }



    def __repr__(self):
        return '<Pictures %r>' % self.id

