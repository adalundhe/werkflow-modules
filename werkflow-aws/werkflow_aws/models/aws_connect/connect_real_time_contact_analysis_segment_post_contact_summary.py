from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectRealTimeContactAnalysisSegmentPostContactSummary(BaseModel):
    Content: StrictStr | None = None
    Status: StrictStr | None = None
    FailureCode: StrictStr | None = None
