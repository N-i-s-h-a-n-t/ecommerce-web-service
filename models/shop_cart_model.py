# from sqlalchemy.orm import relationship

# from . import db
# # from user_model import User

# class Cart(db.Model):
#     __tablename__='cart'
#     cart_id = db.Column(db.Integer, primary_key=True, nullable=False)
#     user_id  = db.Column(db.String(40), ForeignKey=('users.id'),nullable=False)
#     product_id = db.Column(db.String(10), nullable=False)
#     product_name = db.Column(db.String(128), nullable=False)
#     price = db.Column(db.String(64), nullable=False)
#     quantity = db.Column(db.String(20), nullable=False)
#     tax = db.Column(db.Integer, nullable=False)
#     # parent = relationship(User)
