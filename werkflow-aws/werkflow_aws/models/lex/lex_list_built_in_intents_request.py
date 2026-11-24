from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .lex_built_in_intent_sort_by import LexBuiltInIntentSortBy


class LexListBuiltInIntentsRequest(BaseModel):
    localeId: StrictStr
    sortBy: LexBuiltInIntentSortBy | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
