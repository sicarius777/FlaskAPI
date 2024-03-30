from marshmallow import Schema, fields

class PostSchema(Schema):
    id = fields.Str(dump_only=True)
    title = fields.Str()
    body = fields.Str(required=True)
    user_id = fields.Int(required=True)

class UserSchema(Schema):
    id = fields.Str(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True, load_only = True)
    first_name= fields.Str()
    last_name= fields.Str()

class PostWithUserSchema(PostSchema):
    author = fields.Nested(UserSchema)

class UserWithPostsSchema(UserSchema):
    posts = fields.List(fields.Nested(PostSchema), dump_only = True)


class ShipSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    classification = fields.String(required=True)
    length = fields.Float(required=True)
    faction_id = fields.Integer(required=True)

class ShipWithFactionSchema(ShipSchema):
    faction = fields.Nested('FactionSchema', only=('id', 'name'))

class ArmorSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    description = fields.String()
    armor_class = fields.String(required=True)
    defense_rating = fields.Integer(required=True)
    weight = fields.Float()
    owner_id = fields.Integer(required=True)

class ArmorWithOwnerSchema(ArmorSchema):
    owner = fields.Nested('CharacterSchema', only=('id', 'name'))