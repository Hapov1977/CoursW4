from contextlib import suppress
from curses import wrapper
from functools import wraps

import jwt
from flask import current_app, request
from jwt import PyJWTError

from project.exceptions import ItemNotFound

from project.jwt_token import JwtToken


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        if auth_header := request.headers.get('Authorization'):
           token: str = auth_header.split('Bearer ')[-1]

            with suppress(PyJWTError):
                if user_id := JwtToken.decode(token).get('id'):
                    return func(user_id=user_id, *args, **kwargs)
        raise ItemNotFound
    return wrapper