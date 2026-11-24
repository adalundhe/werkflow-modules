from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .comprehend_batch_detect_targeted_sentiment_item_result import ComprehendBatchDetectTargetedSentimentItemResult
from .comprehend_batch_item_error import ComprehendBatchItemError


class ComprehendBatchDetectTargetedSentimentResponse(BaseModel):
    ResultList: list[ComprehendBatchDetectTargetedSentimentItemResult] | None = None
    ErrorList: list[ComprehendBatchItemError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
