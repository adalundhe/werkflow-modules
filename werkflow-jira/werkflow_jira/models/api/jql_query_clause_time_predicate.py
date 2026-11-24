from __future__ import annotations
from typing import TYPE_CHECKING
from pydantic import BaseModel, StrictStr

if TYPE_CHECKING:
    from .jql_query_clause_operand import JqlQueryClauseOperand


class JqlQueryClauseTimePredicate(BaseModel):
    operand: JqlQueryClauseOperand | None = None
    operator: StrictStr | None = None
