from requests import get

from jose import jwt


def get_keys(region="us-west-2", user_pool_id="us-west-2_kVyMu9Hd9"):
    keys_url = f"https://cognito-idp.{region}.amazonaws.com/{user_pool_id}/.well-known/jwks.json"
    response = get(keys_url)
    return response.json()


def find_key(key_id):
    keys_json = get_keys()
    key_dict = {key["kid"]: key for key in keys_json["keys"]}
    return key_dict.get(key_id)


def validate_token(token, alg="RS256"):
    key_id = jwt.get_unverified_headers(token).get("kid")
    key = find_key(key_id)
    return jwt.decode(token, key, alg)
