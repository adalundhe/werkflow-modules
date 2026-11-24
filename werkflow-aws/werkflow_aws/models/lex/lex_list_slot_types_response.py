from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_slot_type_summary import LexSlotTypeSummary


class LexListSlotTypesResponse(BaseModel):
    botId: StrictStr | None = None
    botVersion: StrictStr | None = None
    localeId: StrictStr | None = None
    slotTypeSummaries: list[LexSlotTypeSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
