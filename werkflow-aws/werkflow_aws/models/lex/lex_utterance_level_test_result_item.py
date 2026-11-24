from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .lex_test_set_turn_result import LexTestSetTurnResult


class LexUtteranceLevelTestResultItem(BaseModel):
    recordNumber: StrictInt | None = None
    conversationId: StrictStr | None = None
    turnResult: LexTestSetTurnResult | None = None
