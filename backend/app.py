"""
Create the application.

"""
from microcosm.api import create_object_graph
from microcosm.loaders import load_each, load_from_environ, load_from_json_file
from microcosm.loaders.compose import load_config_and_secrets
from microcosm.metadata import Metadata

import backend.postgres  # noqa: F401
import backend.routes  # noqa: F401
import backend.stores  # noqa: F401
from backend.config import load_default_config


def load_secrets(metadata):
    """
    Load secrets using injected environment variables.

    Generate an "internal" naming prefix to differentiate secrets from other config.

    """
    return load_from_environ(Metadata(f"_{metadata.name}"))


def create_app(debug=False, testing=False, model_only=False):
    """
    Create the object graph for the application.

    """
    config_loader = load_each(
        load_default_config,
        load_from_environ,
        load_from_json_file,
    )

    partitioned_loader = load_config_and_secrets(
        config=config_loader,
        secrets=load_secrets,
    )

    graph = create_object_graph(
        name=__name__.split(".")[0],
        debug=debug,
        testing=testing,
        loader=partitioned_loader,
    )

    graph.use(
        "logging",
        "postgres",
        "sessionmaker",
        "session_factory",
        # stores
        "account_store",
    )

    if not model_only:
        graph.use(
            # conventions
            "build_info_convention",
            "config_convention",
            "discovery_convention",
            "health_convention",
            "landing_convention",
            "port_forwarding",
            "postgres_health_check",
            "swagger_convention",
            # routes
            "account_routes",
        )

    return graph.lock()
