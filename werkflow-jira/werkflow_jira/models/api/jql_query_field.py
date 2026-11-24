from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .jql_query_field_entity_property import JqlQueryFieldEntityProperty


class JqlQueryField(BaseModel):
    encodedName: StrictStr | None = None
    name: StrictStr | None = None
    property: list[JqlQueryFieldEntityProperty] | None = None
