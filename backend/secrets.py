from json import loads

from boto3 import Session


def load_secrets(metadata):
    """
    Placeholder for secrets loading.

    The usual microcosm-secretsmanager was not working properly even though it has the
    exact same logic. It may make sense to switch to an environment loader with a different
    prefix and ECS secrets support.

    """
    try:
        session = Session()
        secretsmanager = session.client("secretsmanager")
        response = secretsmanager.get_secret_value(
            SecretId="secrets//backend",
            VersionStage="AWSCURRENT",
        )
        data = loads(response["SecretString"])
        return data.get("config", {})
    except Exception:
        return {}
