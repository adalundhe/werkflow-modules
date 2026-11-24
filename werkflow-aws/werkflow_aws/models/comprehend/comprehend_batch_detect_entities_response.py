from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .comprehend_batch_detect_entities_item_result import ComprehendBatchDetectEntitiesItemResult
from .comprehend_batch_item_error import ComprehendBatchItemError


class ComprehendBatchDetectEntitiesResponse(BaseModel):
    ResultList: list[ComprehendBatchDetectEntitiesItemResult] | None = None
    ErrorList: list[ComprehendBatchItemError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
