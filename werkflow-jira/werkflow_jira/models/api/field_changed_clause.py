from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .jql_query_clause_time_predicate import JqlQueryClauseTimePredicate
from .jql_query_field import JqlQueryField


class FieldChangedClause(BaseModel):
    field: JqlQueryField | None = None
    operator: StrictStr | None = None
    predicates: list[JqlQueryClauseTimePredicate] | None = None
