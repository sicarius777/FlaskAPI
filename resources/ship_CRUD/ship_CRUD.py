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

    @staticmethod
    def create_ship(name, classification, length, faction_id):
        ship = Ship(name=name, classification=classification, length=length, faction_id=faction_id)
        db.session.add(ship)
        db.session.commit()
        return ship

    @staticmethod
    def get_ship_by_id(ship_id):
        return Ship.query.get(ship_id)

    @staticmethod
    def update_ship(ship_id, name=None, classification=None, length=None, faction_id=None):
        ship = Ship.get_ship_by_id(ship_id)
        if ship:
            if name:
                ship.name = name
            if classification:
                ship.classification = classification
            if length:
                ship.length = length
            if faction_id:
                ship.faction_id = faction_id
            db.session.commit()
        return ship

    @staticmethod
    def delete_ship(ship_id):
        ship = Ship.get_ship_by_id(ship_id)
        if ship:
            db.session.delete(ship)
            db.session.commit()
            return True
        return False
