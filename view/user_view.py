from flask_restx import Resource, Namespace, fields, reqparse
from dao import get_users, add_user

api = Namespace("users", description="User Operations")

user = api.model(
    "User",
    {
        "id": fields.Integer(description="The unique identifier of the user"),
        "username": fields.String(description="The name of the user"),
        "password": fields.String(description="The email address of the user"),
        "email": fields.String(description="The password of the user"),
    },
)


@api.route("/")
class UserList(Resource):
    @api.doc(responses={403: "not authorized", 200: "success"})
    @api.marshal_list_with(user)
    def get(self):
        """List of users"""
        return get_users()


@api.route("/add")
class AddUser(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", required=True)
    parser.add_argument("password", required=True)
    parser.add_argument("email", required=True)

    @api.doc(responses={403: "not authorized"})
    @api.expect(parser)
    def post(self):
        """Add new user"""
        args = self.parser.parse_args()
        add_user(args)
        return ({"messasge": "User added sucessfully"}, 201)
