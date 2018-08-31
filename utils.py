from app import db, User, Prayer

def validate_user_new(username):
    if User.query.filter_by(username=username).first() != None:
        return False
    return True
    