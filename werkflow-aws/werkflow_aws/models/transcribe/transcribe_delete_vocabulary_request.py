from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranscribeDeleteVocabularyRequest(BaseModel):
    VocabularyName: StrictStr
