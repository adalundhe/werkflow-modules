from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_qa_result import QuickSightQAResult


class QuickSightPredictQAResultsResponse(BaseModel):
    PrimaryResult: QuickSightQAResult | None = None
    AdditionalResults: list[QuickSightQAResult] | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
