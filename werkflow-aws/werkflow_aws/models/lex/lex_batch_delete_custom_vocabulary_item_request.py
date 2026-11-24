from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_custom_vocabulary_entry_id import LexCustomVocabularyEntryId


class LexBatchDeleteCustomVocabularyItemRequest(BaseModel):
    botId: StrictStr
    botVersion: StrictStr
    localeId: StrictStr
    customVocabularyItemList: list[LexCustomVocabularyEntryId]
