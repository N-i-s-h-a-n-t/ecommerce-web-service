from . import db


class Product(db.Model):
    __tablename__ = "products"
    product_id = db.Column(db.String(10), primary_key=True, nullable=False)
    product_name = db.Column(db.String(40), nullable=False)
    product_image = db.Column(db.LargeBinary, nullable=False)
    product_price = db.Column(db.String(64), nullable=False)
    product_detail = db.relationship("CartDetails", backref="products", lazy=True)
