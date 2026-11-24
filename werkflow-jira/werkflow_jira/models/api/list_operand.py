from __future__ import annotations
from typing import TYPE_CHECKING
from pydantic import BaseModel, StrictStr

if TYPE_CHECKING:
    from .jql_query_unitary_operand import JqlQueryUnitaryOperand


class ListOperand(BaseModel):
    encodedOperand: StrictStr | None = None
    values: list[JqlQueryUnitaryOperand] | None = None
