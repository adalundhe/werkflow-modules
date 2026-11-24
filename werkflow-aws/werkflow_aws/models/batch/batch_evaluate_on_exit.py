from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchEvaluateOnExit(BaseModel):
    onStatusReason: StrictStr | None = None
    onReason: StrictStr | None = None
    onExitCode: StrictStr | None = None
    action: StrictStr | None = None
