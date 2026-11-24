from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingSuspendedProcess(BaseModel):
    ProcessName: StrictStr | None = None
    SuspensionReason: StrictStr | None = None
