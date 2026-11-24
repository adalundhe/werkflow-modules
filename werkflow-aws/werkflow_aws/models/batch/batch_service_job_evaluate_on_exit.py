from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchServiceJobEvaluateOnExit(BaseModel):
    action: StrictStr | None = None
    onStatusReason: StrictStr | None = None
