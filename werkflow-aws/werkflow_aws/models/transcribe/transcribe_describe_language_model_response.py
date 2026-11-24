from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .transcribe_language_model import TranscribeLanguageModel


class TranscribeDescribeLanguageModelResponse(BaseModel):
    LanguageModel: TranscribeLanguageModel | None = None
    ResponseMetadata: dict[str, Any] | None = None
