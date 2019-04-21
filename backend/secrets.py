from json import loads

from boto3 import Session


def load_secrets(metadata):
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
