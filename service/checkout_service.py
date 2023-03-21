from . import Cart, CartDetails
from sqlalchemy.exc import SQLAlchemyError
from service import check_cart


"""Returns the appropriate result whether the user can checkout or not"""


def checkout_cart(user_id):
    try:
        check, status = check_cart(user_id)
        if status:
            if check is None:
                return ({"message": "No Cart for the user"}, True)
        else:
            return (check, status)
        cart_id = (
            Cart.query.filter_by(cart_user_id=user_id, checkout_status="no")
            .first()
            .cart_id
        )
        products = CartDetails.query.filter_by(cart_id=cart_id).all()
        lis = {}
        for product in products:
            prod = product.products
            if prod.product_quantity == 0:
                return (
                    {
                        "message": f"Product({prod.product_name}) is not available. Please remove the product from cart"
                    },
                    True,
                )
            if product.cart_quantity > prod.product_quantity:
                lis[
                    prod.product_name
                ] = f"This much quantity for {prod.product_name} is not present. Please Lower the quantity"
        if lis:
            return (lis, True)
        else:
            return ({"message": "You can place order"}, True)
    except SQLAlchemyError as e:
        error = e.__dict__["orig"]
        return (error, False)
