from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .comprehend_dominant_language import ComprehendDominantLanguage


class ComprehendDetectDominantLanguageResponse(BaseModel):
    Languages: list[ComprehendDominantLanguage] | None = None
    ResponseMetadata: dict[str, Any] | None = None
