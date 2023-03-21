from models import Product


"""this method return list of all products present"""


def get_product():
    product = Product.query.all()
    return product
