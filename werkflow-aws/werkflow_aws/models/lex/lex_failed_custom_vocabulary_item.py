from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexFailedCustomVocabularyItem(BaseModel):
    itemId: StrictStr | None = None
    errorMessage: StrictStr | None = None
    errorCode: StrictStr | None = None
