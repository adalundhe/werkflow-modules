from __future__ import annotations
from typing import TYPE_CHECKING
from pydantic import BaseModel, StrictStr
from .jql_query_clause_time_predicate import JqlQueryClauseTimePredicate
from .jql_query_field import JqlQueryField

if TYPE_CHECKING:
    from .jql_query_clause_operand import JqlQueryClauseOperand


class FieldWasClause(BaseModel):
    field: JqlQueryField | None = None
    operand: JqlQueryClauseOperand | None = None
    operator: StrictStr | None = None
    predicates: list[JqlQueryClauseTimePredicate] | None = None
