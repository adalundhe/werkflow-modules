from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexCustomVocabularyEntryId(BaseModel):
    itemId: StrictStr
