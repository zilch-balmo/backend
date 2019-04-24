"""
Account controller.

"""
from microcosm.api import binding
from microcosm_flask.conventions.crud_adapter import CRUDStoreAdapter
from microcosm_flask.namespaces import Namespace
from microcosm_logging.decorators import logger

from backend.models.account import Account


@logger
@binding("account_controller")
class AccountController(CRUDStoreAdapter):

    def __init__(self, graph):
        super().__init__(graph, graph.account_store)

        self.ns = Namespace(
            subject=Account,
            version="v1",
        )

    def search(self, offset, limit, **kwargs):
        from flask import request
        self.logger.info(f"Request headers:\n{request.headers}")
        return super().search(offset, limit, **kwargs)
