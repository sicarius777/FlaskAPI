ffrom flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from Config import Config
from models.ships import Ship

app = Flask(__name__)

app.config.from_object(Config)
api = Api(app)
jwt = JWTManager(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models.user_model import UserModel
from models.post_model import PostModel
from models.like_post_model import LikePostModel

from resources.post import bp as post_bp
app.register_blueprint(post_bp)
from resources.user import bp as user_bp
app.register_blueprint(user_bp)
from resources.like_post import bp as like_post_bp
app.register_blueprint(like_post_bp)

from ship_CRUD import *

@app.route('/ships', methods=['GET'])
def get_ships():
    ships = Ship.query.all()
    return ship_schema.jsonify(ships)

@app.route('/ships/<int:ship_id>', methods=['GET'])
def get_ship(ship_id):
    ship = Ship.query.get_or_404(ship_id)
    return ship_schema.jsonify(ship)

if __name__ == "__main__":
    app.run()

