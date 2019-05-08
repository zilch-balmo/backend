"""
Account CRUD routes.

"""
from microcosm.api import binding
from microcosm_flask.conventions.base import EndpointDefinition
from microcosm_flask.conventions.crud import configure_crud
from microcosm_flask.operations import Operation
from microcosm_postgres.context import transactional

from backend.resources.account import AccountSchema, NewAccountSchema, SearchAccountSchema
from backend.routes.auth import auth_group


@binding("account_routes")
def configure_account_routes(graph):
    controller = graph.account_controller
    mappings = {
        Operation.Create: EndpointDefinition(
            func=transactional(controller.create),
            request_schema=NewAccountSchema(),
            response_schema=AccountSchema(),
        ),
        Operation.Delete: EndpointDefinition(
            func=transactional(controller.delete),
        ),
        Operation.Retrieve: EndpointDefinition(
            func=auth_group("app-users-group")(controller.retrieve),
            response_schema=AccountSchema(),
        ),
        Operation.Search: EndpointDefinition(
            func=auth_group("app-admins-group")(controller.search),
            request_schema=SearchAccountSchema(),
            response_schema=AccountSchema(),
        ),
    }
    configure_crud(graph, controller.ns, mappings)
    return controller.ns
