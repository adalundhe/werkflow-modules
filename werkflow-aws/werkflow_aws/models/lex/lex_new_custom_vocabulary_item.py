from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LexNewCustomVocabularyItem(BaseModel):
    phrase: StrictStr
    weight: StrictInt | None = None
    displayAs: StrictStr | None = None
