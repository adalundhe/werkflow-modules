from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_analysis import QuickSightAnalysis


class QuickSightDescribeAnalysisResponse(BaseModel):
    Analysis: QuickSightAnalysis | None = None
    Status: StrictInt | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
