from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .transcribe_vocabulary_info import TranscribeVocabularyInfo


class TranscribeListMedicalVocabulariesResponse(BaseModel):
    Status: StrictStr | None = None
    NextToken: StrictStr | None = None
    Vocabularies: list[TranscribeVocabularyInfo] | None = None
    ResponseMetadata: dict[str, Any] | None = None
