from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .comprehend_batch_detect_key_phrases_item_result import ComprehendBatchDetectKeyPhrasesItemResult
from .comprehend_batch_item_error import ComprehendBatchItemError


class ComprehendBatchDetectKeyPhrasesResponse(BaseModel):
    ResultList: list[ComprehendBatchDetectKeyPhrasesItemResult] | None = None
    ErrorList: list[ComprehendBatchItemError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
