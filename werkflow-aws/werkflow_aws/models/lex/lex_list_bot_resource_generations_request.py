from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .lex_generation_sort_by import LexGenerationSortBy


class LexListBotResourceGenerationsRequest(BaseModel):
    botId: StrictStr
    botVersion: StrictStr
    localeId: StrictStr
    sortBy: LexGenerationSortBy | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
