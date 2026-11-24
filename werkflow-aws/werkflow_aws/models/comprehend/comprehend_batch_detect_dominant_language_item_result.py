from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .comprehend_dominant_language import ComprehendDominantLanguage


class ComprehendBatchDetectDominantLanguageItemResult(BaseModel):
    Index: StrictInt | None = None
    Languages: list[ComprehendDominantLanguage] | None = None
