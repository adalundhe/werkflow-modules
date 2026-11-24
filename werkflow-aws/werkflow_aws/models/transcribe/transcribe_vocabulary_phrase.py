from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranscribeVocabularyPhrase(BaseModel):
    Text: StrictStr
    DisplayAs: StrictStr | None = None
