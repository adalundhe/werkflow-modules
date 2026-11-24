from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .jql_query_field import JqlQueryField


class JqlQueryOrderByClauseElement(BaseModel):
    direction: StrictStr | None = None
    field: JqlQueryField | None = None
