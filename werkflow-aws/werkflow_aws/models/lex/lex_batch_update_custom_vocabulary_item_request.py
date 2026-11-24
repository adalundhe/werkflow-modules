from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_custom_vocabulary_item import LexCustomVocabularyItem


class LexBatchUpdateCustomVocabularyItemRequest(BaseModel):
    botId: StrictStr
    botVersion: StrictStr
    localeId: StrictStr
    customVocabularyItemList: list[LexCustomVocabularyItem]
