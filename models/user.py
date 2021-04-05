from db import db

# API cannot receive or send data to this class as JSON
# this class in a helper, which contains functions to retrieve data from db
# internal

# UserModel is an API but not a REST API
class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True) # would be a problem if built-in id method was used
    username = db.Column(db.String(80)) # 80 Character maximum
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        # id is auto created so no need for it here
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username = username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()