import datetime
import time
from flask_jwt import JWTError
from werkzeug.security import safe_str_cmp
from .user import User

users = [
    User(1, "victor", "victor")
]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload["identity"]
    # iat_start = payload["iat"]
    # start = datetime.datetime.fromtimestamp(iat_start)
    # end = datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    #                                  "%Y-%m-%d %H:%M:%S")
    # if (end - start).seconds > setting.JTW_EXPIRE_TIME:
    #     raise JWTError('Invalid token', 'access token had expired')
    return userid_mapping.get(user_id, None)
