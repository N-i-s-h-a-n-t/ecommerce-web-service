from models import db, User
from sqlalchemy.exc import SQLAlchemyError

"""this method return the list of all users"""


def get_users():
    try:
        users = User.query.all()
        return (users, True)
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        return (error, False)


"""this method returns the total number of users"""


def count_of_user():
    try:
        count = User.query.count()
        return (count, True)
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        return (error, False)


"""this method add new user to database"""


def add_user(user):
    res, status = count_of_user()
    if status:
        try:
            new_user = User(
                user_id=res + 1,
                user_name=user.username,
                user_password=user.password,
                user_email=user.email,
            )
            db.session.add(new_user)
            db.session.commit()
            return ("User Added Successfully", True)
        except SQLAlchemyError as e:
            error = str(e.__dict__["orig"])
            return (error, False)
    else:
        return (res, False)
