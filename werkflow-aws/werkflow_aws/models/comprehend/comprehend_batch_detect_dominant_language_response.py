from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .comprehend_batch_detect_dominant_language_item_result import ComprehendBatchDetectDominantLanguageItemResult
from .comprehend_batch_item_error import ComprehendBatchItemError


class ComprehendBatchDetectDominantLanguageResponse(BaseModel):
    ResultList: list[ComprehendBatchDetectDominantLanguageItemResult] | None = None
    ErrorList: list[ComprehendBatchItemError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
