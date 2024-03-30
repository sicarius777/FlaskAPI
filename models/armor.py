from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Armor(db.Model):
    __tablename__ = 'armor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    armor_class = db.Column(db.String(50), nullable=False)
    defense_rating = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Float)
    owner_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    owner = db.relationship('Character', back_populates='armor')

class Character(db.Model):
    __tablename__ = 'characters'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(100))
    affiliation = db.Column(db.String(100))
    armor = db.relationship('Armor', back_populates='owner')
