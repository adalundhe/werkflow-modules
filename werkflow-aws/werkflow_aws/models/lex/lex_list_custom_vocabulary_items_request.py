from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LexListCustomVocabularyItemsRequest(BaseModel):
    botId: StrictStr
    botVersion: StrictStr
    localeId: StrictStr
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
