"""
Account CRUD routes tests.

"""
from unittest.mock import patch

from hamcrest import (
    assert_that,
    contains,
    equal_to,
    has_entries,
    is_,
)
from microcosm_postgres.context import SessionContext, transaction
from microcosm_postgres.identifiers import new_object_id
from microcosm_postgres.operations import recreate_all

from backend.app import create_app
from backend.models.account import Account


class TestAccountRoutes:

    def setup(self):
        self.graph = create_app(testing=True)
        self.client = self.graph.flask.test_client()
        recreate_all(self.graph)

        self.name = "name"

        self.account = Account(
            id=new_object_id(),
            name=self.name,
        )

    def teardown(self):
        self.graph.postgres.dispose()

    def test_search(self):
        with SessionContext(self.graph), transaction():
            self.account.create()

        uri = "/api/v1/account"

        response = self.client.get(uri)

        assert_that(response.status_code, is_(equal_to(200)))
        assert_that(
            response.json,
            has_entries(
                items=contains(
                    has_entries(
                        id=str(self.account.id),
                        name=self.account.name,
                    ),
                ),
            ),
        )

    def test_create(self):
        uri = "/api/v1/account"

        with patch.object(self.graph.account_store, "new_object_id") as mocked:
            mocked.return_value = self.account.id
            response = self.client.post(
                uri,
                json=dict(
                    name=self.account.name,
                ),
            )

        assert_that(response.status_code, is_(equal_to(201)))
        assert_that(
            response.json,
            has_entries(
                id=str(self.account.id),
                name=self.account.name,
            ),
        )

    def test_retrieve(self):
        with SessionContext(self.graph), transaction():
            self.account.create()

        uri = f"/api/v1/account/{self.account.id}"

        response = self.client.get(uri)

        assert_that(
            response.json,
            has_entries(
                id=str(self.account.id),
                name=self.account.name,
            ),
        )

    def test_delete(self):
        with SessionContext(self.graph), transaction():
            self.account.create()

        uri = f"/api/v1/account/{self.account.id}"

        response = self.client.delete(uri)
        assert_that(response.status_code, is_(equal_to(204)))
