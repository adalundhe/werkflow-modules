from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranscribeGetVocabularyRequest(BaseModel):
    VocabularyName: StrictStr
