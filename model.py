from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """Data model for a user"""

    __tablename__ = "users"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)

    reservations = db.relationship("Reservation", back_populates="user")

    def __repr__(self):
        return f"<user_id={self.id} username={self.username}>"


class Reservation(db.Model):
    """Data model for user's reservations."""

    __tablename__ = "reservations"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    reservation_date = db.Column(db.DateTime, nullable=False)
    reservation_time = db.Column(db.Time, nullable=False)
    is_not_available = db.Column(db.Boolean, default=True)

    user = db.relationship("User", back_populates="reservations")

    def __repr__(self):
        return f"<Reservation id={self.id} date={self.reservation_date} time={self.reservation_time}>"

def connect_to_db(app):
    """Connect the database to Flask app."""

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///reservations_db"
    app.config["SQLALCHEMY_ECHO"] = False
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    print("Connected to db!")


if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)
    connect_to_db(app)
    