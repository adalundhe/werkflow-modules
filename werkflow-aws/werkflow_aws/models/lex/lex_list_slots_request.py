from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .lex_slot_filter import LexSlotFilter
from .lex_slot_sort_by import LexSlotSortBy


class LexListSlotsRequest(BaseModel):
    botId: StrictStr
    botVersion: StrictStr
    localeId: StrictStr
    intentId: StrictStr
    sortBy: LexSlotSortBy | None = None
    filters: list[LexSlotFilter] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
