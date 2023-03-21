from flask_restx import Resource, Namespace, fields
from dao import get_product

api = Namespace("product", description="Product Operations")

product = api.model(
    "Product",
    {
        "product_id": fields.String(description="The unique identifier of the product"),
        "product_name": fields.String(description="The name of product"),
        "product_image": fields.String(description="The Image of product"),
        "product_price": fields.Float(description="The Price of product"),
    },
)


@api.route("/")
class CartList(Resource):
    @api.doc(responses={403: "not authorized", 200: "success"})
    @api.marshal_list_with(product)
    def get(self):
        """List of products"""
        return get_product()
