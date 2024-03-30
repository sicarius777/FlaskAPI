from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Ship(db.Model):
    __tablename__ = 'ships'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    classification = db.Column(db.String(50), nullable=False)
    length = db.Column(db.Float, nullable=False)
    # Add more attributes as needed

    faction_id = db.Column(db.Integer, db.ForeignKey('factions.id'), nullable=False)
    faction = db.relationship('Faction', back_populates='ships')

class Faction(db.Model):
    __tablename__ = 'factions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    ships = db.relationship('Ship', back_populates='faction')
