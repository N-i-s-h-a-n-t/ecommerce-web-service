from models import db, User


def get_users():
    users = User.query.all()
    return users


def count_of_user():
    count = User.query.count()
    return count


def add_user(user):
    count = User.query.count()
    new_user = User(
        id=count + 1,
        username=user.username,
        password=user.password,
        email=user.email
    )
    db.session.add(new_user)
    db.session.commit()
