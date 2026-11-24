from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .iam_evaluation_result import IAMEvaluationResult


class IAMSimulateCustomPolicyResponse(BaseModel):
    EvaluationResults: list[IAMEvaluationResult] | None = None
    IsTruncated: StrictBool | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
