from flask_restx import Resource, Namespace, fields, reqparse
from dao import add_product

api = Namespace("product", description="Product Operations")

product = api.model(
    "Product",
    {
        "product_id": fields.String(description="The unique identifier of the product"),
        "product_name": fields.String(description="The name of product"),
        "product_image": fields.String(description="The Image of product"),
        "product_price": fields.Float(description="The Price of product"),
        "product_quantity": fields.Integer(description="The Product Quantity"),
        "product_tax": fields.Integer(description="The Product Tax"),
    },
)


@api.route("/addProduct")  # Add new product into product table
class AddProduct(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("product_name", required=True)
    parser.add_argument("product_image", required=True)
    parser.add_argument("product_price", required=True)
    parser.add_argument("product_quantity", required=True)
    parser.add_argument("product_tax", required=True)

    @api.doc(
        responses={
            200: "success",
            201: "Created",
            204: "No Content",
            400: "Bad Request",
            404: "Not Found",
            500: "Internal Server Error",
        },
        description="This API will add new product",
    )
    @api.expect(parser)
    def post(self):
        """Add new Product"""
        args = self.parser.parse_args()
        res, status = add_product(args)
        if status:
            return ({"messasge": res}, 201)
        else:
            return (
                {"message": "Server Error please try again later", "error": res},
                500,
            )
