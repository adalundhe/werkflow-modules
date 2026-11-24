from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_new_custom_vocabulary_item import LexNewCustomVocabularyItem


class LexBatchCreateCustomVocabularyItemRequest(BaseModel):
    botId: StrictStr
    botVersion: StrictStr
    localeId: StrictStr
    customVocabularyItemList: list[LexNewCustomVocabularyItem]
