from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .lex_bot_version_sort_by import LexBotVersionSortBy


class LexListBotVersionsRequest(BaseModel):
    botId: StrictStr
    sortBy: LexBotVersionSortBy | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
