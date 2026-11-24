from __future__ import annotations
from pydantic import BaseModel
from .jql_query_order_by_clause_element import JqlQueryOrderByClauseElement


class JqlQueryOrderByClause(BaseModel):
    fields: list[JqlQueryOrderByClauseElement] | None = None
