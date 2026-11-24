from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .transcribe_tag import TranscribeTag


class TranscribeCreateMedicalVocabularyRequest(BaseModel):
    VocabularyName: StrictStr
    LanguageCode: StrictStr
    VocabularyFileUri: StrictStr
    Tags: list[TranscribeTag] | None = None
