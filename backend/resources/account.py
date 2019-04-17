"""
Account resources.

"""
from marshmallow import Schema, fields
from microcosm_flask.linking import Link, Links
from microcosm_flask.namespaces import Namespace
from microcosm_flask.operations import Operation
from microcosm_flask.paging import PageSchema

from backend.models.account import Account


class NewAccountSchema(Schema):
    name = fields.String(
        required=True,
    )


class AccountSchema(NewAccountSchema):
    id = fields.UUID(
        required=True,
    )
    _links = fields.Method(
        "get_links",
        dump_only=True,
    )

    def get_links(self, obj):
        links = Links()
        links["self"] = Link.for_(
            Operation.Retrieve,
            Namespace(
                subject=Account,
                version="v1",
            ),
            account_id=obj.id,
        )
        return links.to_dict()


class SearchAccountSchema(PageSchema):
    name = fields.String()
