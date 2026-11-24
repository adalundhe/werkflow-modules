from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .comprehend_batch_detect_sentiment_item_result import ComprehendBatchDetectSentimentItemResult
from .comprehend_batch_item_error import ComprehendBatchItemError


class ComprehendBatchDetectSentimentResponse(BaseModel):
    ResultList: list[ComprehendBatchDetectSentimentItemResult] | None = None
    ErrorList: list[ComprehendBatchItemError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
