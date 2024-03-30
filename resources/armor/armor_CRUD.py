from flask.views import MethodView
from flask_smorest import abort

from flask_jwt_extended import jwt_required

from . import bp
from schemas import ArmorSchema
from models import Armor

@bp.route('/armor')
class ArmorList(MethodView):
    
    @jwt_required()
    @bp.response(201, ArmorSchema)
    @bp.arguments(ArmorSchema)
    def post(self, armor_data):

        try:
            armor = Armor()
            armor.from_dict(armor_data)

            armor.save_armor()

            return armor
        except:
            abort(400, message=f"{armor.name} failed to post")

    @bp.response(200, ArmorSchema(many=True))
    def get(self):
        return Armor.query.all()

@bp.route('/armor/<armor_id>')
class Armor(MethodView):

    @bp.response(200, ArmorSchema)
    def get(self, armor_id):
        try: 
            return Armor.query.get(armor_id)
        except:
            abort(400, message="Armor not found")

    @bp.arguments(ArmorSchema)
    @bp.response(201, ArmorSchema)
    def put(self, armor_data, armor_id):
            
        armor = Armor.query.get(armor_id)
        if not armor:
            abort(400, message="Armor not found")

        armor.from_dict(armor_data)
        armor.save_armor()
        return armor

    def delete(self, armor_id):

        armor = Armor.query.get(armor_id)
        if not armor:
            abort(400, message="Armor not found")
        
        armor.del_armor()
        return {'message': f'Armor: {armor_id} deleted'}, 200

