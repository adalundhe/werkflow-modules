from __future__ import annotations
from typing import TYPE_CHECKING
from pydantic import BaseModel
from .jql_query_order_by_clause import JqlQueryOrderByClause

if TYPE_CHECKING:
    from .jql_query_clause import JqlQueryClause


class JqlQuery(BaseModel):
    orderBy: JqlQueryOrderByClause | None = None
    where: JqlQueryClause | None = None
