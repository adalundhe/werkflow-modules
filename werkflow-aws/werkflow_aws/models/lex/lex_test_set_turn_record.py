from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .lex_turn_specification import LexTurnSpecification


class LexTestSetTurnRecord(BaseModel):
    recordNumber: StrictInt | None = None
    conversationId: StrictStr | None = None
    turnNumber: StrictInt | None = None
    turnSpecification: LexTurnSpecification | None = None
