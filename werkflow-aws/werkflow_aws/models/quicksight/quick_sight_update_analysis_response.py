from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightUpdateAnalysisResponse(BaseModel):
    Arn: StrictStr | None = None
    AnalysisId: StrictStr | None = None
    UpdateStatus: StrictStr | None = None
    Status: StrictInt | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
