from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_custom_vocabulary_item import LexCustomVocabularyItem


class LexListCustomVocabularyItemsResponse(BaseModel):
    botId: StrictStr | None = None
    botVersion: StrictStr | None = None
    localeId: StrictStr | None = None
    customVocabularyItems: list[LexCustomVocabularyItem] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
