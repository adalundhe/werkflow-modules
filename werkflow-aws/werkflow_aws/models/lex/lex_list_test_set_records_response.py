from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_test_set_turn_record import LexTestSetTurnRecord


class LexListTestSetRecordsResponse(BaseModel):
    testSetRecords: list[LexTestSetTurnRecord] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
