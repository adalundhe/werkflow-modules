from __future__ import annotations
from typing import TYPE_CHECKING
from pydantic import BaseModel, StrictStr

if TYPE_CHECKING:
    from .jql_query_clause import JqlQueryClause


class CompoundClause(BaseModel):
    clauses: list[JqlQueryClause] | None = None
    operator: StrictStr | None = None
