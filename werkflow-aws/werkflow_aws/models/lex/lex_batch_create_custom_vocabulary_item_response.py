from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_custom_vocabulary_item import LexCustomVocabularyItem
from .lex_failed_custom_vocabulary_item import LexFailedCustomVocabularyItem


class LexBatchCreateCustomVocabularyItemResponse(BaseModel):
    botId: StrictStr | None = None
    botVersion: StrictStr | None = None
    localeId: StrictStr | None = None
    errors: list[LexFailedCustomVocabularyItem] | None = None
    resources: list[LexCustomVocabularyItem] | None = None
    ResponseMetadata: dict[str, Any] | None = None
