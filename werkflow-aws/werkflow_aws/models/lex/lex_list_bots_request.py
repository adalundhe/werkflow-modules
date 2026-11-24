from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .lex_bot_filter import LexBotFilter
from .lex_bot_sort_by import LexBotSortBy


class LexListBotsRequest(BaseModel):
    sortBy: LexBotSortBy | None = None
    filters: list[LexBotFilter] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
