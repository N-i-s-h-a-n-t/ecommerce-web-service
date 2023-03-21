from models import db, Cart, CartDetails, Product
from service import (
    addtocartdetail,
    check_cart,
    deletefromcart,
    check_user,
    check_product,
    create_cart,
)
from sqlalchemy.exc import SQLAlchemyError


"""This method will return the cart detail for a particular user"""


def get_cart(id):
    try:
        res, status = check_user(id)
        if status:
            if res == "no":
                return (res, True)
            cart = Cart.query.filter_by(cart_user_id=id).first()
            if cart:
                return (cart, True)
            else:
                return ("None", True)
        return (res, False)
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        return (error, False)


"""This method will add product to cart for a particular user"""


def addtocart(product, user_id):
    user, status = check_user(user_id)
    if status:
        if user == "no":
            return (user, True)
    else:
        return (user, False)
    cart_id, cart_status = check_cart(user_id)
    if cart_status:
        if cart_id is None:
            cart_id = create_cart(user_id)
    else:
        return (cart_id, False)
    check_pd, status = check_product(product.product_id)
    if status:
        if check_pd is None:
            return ({"message": "Product does not exist"}, True)
    else:
        return (check_pd, False)
    result, stats = addtocartdetail(cart_id, product)
    return (result, stats)


"""This method will remove product from a cart for a particular user"""


def removefromcart(user_id, cart):
    user, status = check_user(user_id)
    if status:
        if user == "no":
            return (user, True)
    else:
        return (user, False)
    product, status = check_product(cart.product_id)
    if not status:
        return (product, False)
    cart_id, cart_status = check_cart(user_id)
    if cart_status:
        if cart_id is None:
            return ({"message": "Cart Does not exist"}, True)
    else:
        return (cart_id, False)
    res, status = deletefromcart(cart_id, cart)
    return res, status


"""This method will update a product item in cart for a particular user"""


def updatecart(user_id, cart):
    try:
        user, status = check_user(user_id)
        if status:
            if user == "no":
                return (user, True)
        else:
            return (user, False)
        check, status = check_cart(user_id)
        if status:
            cart_id = check
        else:
            return (check, True)
        product, status = check_product(cart.product_id)
        if not status:
            return (product, True)

        cartdetails = CartDetails.query.filter_by(
            cart_id=cart_id, cart_product_id=cart.product_id
        ).first()
        if not cartdetails:
            return ({"message": "No Product in Cart"}, True)
        product_price = (
            Product.query.filter_by(product_id=cart.product_id).first().product_price
        )
        cart_data = Cart.query.filter_by(cart_id=cart_id).first()
        cartdetails.cart_quantity = cart.quantity
        cartdetails.cart_price = product_price * cartdetails.cart_quantity
        cart_data.cart_amount = cart_data.cart_amount + cartdetails.cart_price
        db.session.commit()
        return ({"message": "Product updated in cart successfully"}, True)
    except SQLAlchemyError as e:
        error = e.__dict__["orig"]
        return (error, False)
