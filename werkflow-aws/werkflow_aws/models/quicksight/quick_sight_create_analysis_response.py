from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightCreateAnalysisResponse(BaseModel):
    Arn: StrictStr | None = None
    AnalysisId: StrictStr | None = None
    CreationStatus: StrictStr | None = None
    Status: StrictInt | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
