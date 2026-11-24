from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_slot_summary import LexSlotSummary


class LexListSlotsResponse(BaseModel):
    botId: StrictStr | None = None
    botVersion: StrictStr | None = None
    localeId: StrictStr | None = None
    intentId: StrictStr | None = None
    slotSummaries: list[LexSlotSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
