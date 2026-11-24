from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .lex_slot_type_filter import LexSlotTypeFilter
from .lex_slot_type_sort_by import LexSlotTypeSortBy


class LexListSlotTypesRequest(BaseModel):
    botId: StrictStr
    botVersion: StrictStr
    localeId: StrictStr
    sortBy: LexSlotTypeSortBy | None = None
    filters: list[LexSlotTypeFilter] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
