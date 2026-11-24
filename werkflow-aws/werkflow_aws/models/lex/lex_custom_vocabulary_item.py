from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LexCustomVocabularyItem(BaseModel):
    itemId: StrictStr | None = None
    phrase: StrictStr | None = None
    weight: StrictInt | None = None
    displayAs: StrictStr | None = None
