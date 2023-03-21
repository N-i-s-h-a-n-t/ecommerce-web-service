from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user_dao import get_users, count_of_user, add_user
from .cart_dao import get_cart, addtocart, removefromcart, updatecart
from .product_dao import get_product
