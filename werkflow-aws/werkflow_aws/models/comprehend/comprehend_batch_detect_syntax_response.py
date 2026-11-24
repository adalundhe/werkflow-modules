from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .comprehend_batch_detect_syntax_item_result import ComprehendBatchDetectSyntaxItemResult
from .comprehend_batch_item_error import ComprehendBatchItemError


class ComprehendBatchDetectSyntaxResponse(BaseModel):
    ResultList: list[ComprehendBatchDetectSyntaxItemResult] | None = None
    ErrorList: list[ComprehendBatchItemError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
