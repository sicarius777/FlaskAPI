from flask import request, jsonify
from flask_smorest import abort
from uuid import uuid4
from flask_jwt_extended import create_access_token, unset_jwt_cookies
from flask.views import MethodView

from schemas import UserSchema, UserWithPostsSchema
from . import bp
from models.user_model import UserModel

@bp.route('/user')
class UserList(MethodView):
    
    @bp.response(200, UserWithPostsSchema(many=True))
    def get(self):
        return UserModel.query.all()

    
    @bp.arguments(UserSchema)
    @bp.response(201, UserSchema)
    def post(self, data):
        try:
            user = UserModel()
            user.from_dict(data)
            user.save_user()
            return user
        except:
            abort(400, message="username or email already taken, please try a different one!")

        
@bp.route('/user/<int:id>')
class User(MethodView):
    
    @bp.response(200, UserWithPostsSchema)
    def get(self, id):
        user = UserModel.query.get(id)
        if user:
            return user
        else:
            abort(400, message="not a valid user")


    @bp.arguments(UserSchema)
    @bp.response(200, UserWithPostsSchema)
    def put(self, data, id):
        user = UserModel.query.get(id)
        if user:
            user.from_dict(data)
            user.save_user()
            return user
        else:
            abort(400, message="not a valid user")          


    def delete(self, id):
        user = UserModel.query.get(id)
        if user:
            user.del_user()
            return { "message": "user GONE GONE GONE"}, 200
        abort(400, message="not a valid user")

@bp.post('/login')
def login():
    login_data = request.get_json()
    username = login_data['username']

    user = UserModel.query.filter_by(username = username).first()
    if user and user.check_password( login_data['password'] ):
        access_token = create_access_token(identity=user.id)
        return {'access_token': access_token}, 201

    abort(400, message="Invalid User Data")

@bp.route("/logout", methods=["POST"])
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response