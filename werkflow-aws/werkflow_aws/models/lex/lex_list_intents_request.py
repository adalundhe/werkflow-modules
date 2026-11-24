from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .lex_intent_filter import LexIntentFilter
from .lex_intent_sort_by import LexIntentSortBy


class LexListIntentsRequest(BaseModel):
    botId: StrictStr
    botVersion: StrictStr
    localeId: StrictStr
    sortBy: LexIntentSortBy | None = None
    filters: list[LexIntentFilter] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
