from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .lex_bot_locale_filter import LexBotLocaleFilter
from .lex_bot_locale_sort_by import LexBotLocaleSortBy


class LexListBotLocalesRequest(BaseModel):
    botId: StrictStr
    botVersion: StrictStr
    sortBy: LexBotLocaleSortBy | None = None
    filters: list[LexBotLocaleFilter] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
