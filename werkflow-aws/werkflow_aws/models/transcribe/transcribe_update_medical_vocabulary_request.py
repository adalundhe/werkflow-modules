from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranscribeUpdateMedicalVocabularyRequest(BaseModel):
    VocabularyName: StrictStr
    LanguageCode: StrictStr
    VocabularyFileUri: StrictStr
