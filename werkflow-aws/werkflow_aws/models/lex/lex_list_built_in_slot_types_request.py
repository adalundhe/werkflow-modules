from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .lex_built_in_slot_type_sort_by import LexBuiltInSlotTypeSortBy


class LexListBuiltInSlotTypesRequest(BaseModel):
    localeId: StrictStr
    sortBy: LexBuiltInSlotTypeSortBy | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
