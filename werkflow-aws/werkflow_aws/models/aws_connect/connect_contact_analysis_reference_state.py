from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectContactAnalysisReferenceState(BaseModel):
    Status: StrictStr | None = None
    StatusReason: StrictStr | None = None
