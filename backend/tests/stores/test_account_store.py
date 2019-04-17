"""
Account persistence tests.

"""
from hamcrest import (
    assert_that,
    calling,
    equal_to,
    is_,
    raises,
)
from microcosm_postgres.context import SessionContext, transaction
from microcosm_postgres.errors import DuplicateModelError

from backend.app import create_app
from backend.models.account import Account


class TestAccountStore:

    def setup(self):
        self.graph = create_app(testing=True)
        self.account_store = self.graph.account_store

        self.name = "NAME"

        with SessionContext(self.graph) as context:
            context.recreate_all()

    def teardown(self):
        self.graph.postgres.dispose()

    def test_create(self):
        """
        Accounts can be persisted.

        """
        new_account = Account(
            name=self.name,
        )

        with SessionContext(self.graph):
            with transaction():
                self.account_store.create(new_account)

            retrieved_account = self.account_store.retrieve(new_account.id)
            assert_that(retrieved_account, is_(equal_to(new_account)))

    def test_create_duplicate(self):
        """
        Accounts enforce uniqueness on type/external id.

        """
        account1 = Account(
            name=self.name,
        )
        account2 = Account(
            name=self.name,
        )

        with SessionContext(self.graph):
            with transaction():
                self.account_store.create(account1)

            assert_that(
                calling(self.account_store.create).with_args(account2),
                raises(DuplicateModelError),
            )
