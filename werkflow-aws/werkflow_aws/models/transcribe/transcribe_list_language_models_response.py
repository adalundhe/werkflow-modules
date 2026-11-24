from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .transcribe_language_model import TranscribeLanguageModel


class TranscribeListLanguageModelsResponse(BaseModel):
    NextToken: StrictStr | None = None
    Models: list[TranscribeLanguageModel] | None = None
    ResponseMetadata: dict[str, Any] | None = None
