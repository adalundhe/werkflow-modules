from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranscribeGetVocabularyFilterRequest(BaseModel):
    VocabularyFilterName: StrictStr
