"""
Account persistence.

"""
from microcosm.api import binding
from microcosm_postgres.store import Store

from backend.models.account import Account


@binding("account_store")
class AccountStore(Store):

    def __init__(self, graph):
        super().__init__(self, Account, [
            Account.name,
        ])

    def _order_by(self, query, **kwargs):
        return query.order_by(
            Account.name.asc(),
        )
