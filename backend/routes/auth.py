"""
Decorator for granting access based on user group

"""
from base64 import b64decode
from json import loads

from flask import request
from werkzeug.exceptions import Unauthorized


def auth_group(group):
    def wrapped(func):
        def inner(*args, **kwargs):
            if validate_auth(group):
                return func(*args, **kwargs)
        return inner
    return wrapped


def parse_groups():
    """
    Returns list of cognito groups from request

    Note: Still need to implement jwt signature validation

    """
    oidc_data = request.headers.get("x-amzn-oidc-data")
    if not oidc_data:
        return []
    jwt_claims = oidc_data.split(".")[1]
    claims = loads(b64decode(jwt_claims))
    return claims.get("cognito:groups", [])


def validate_auth(group):
    groups = parse_groups()
    if group in groups:
        return True
    raise Unauthorized
