from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranscribeDeleteMedicalVocabularyRequest(BaseModel):
    VocabularyName: StrictStr
