from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2SendDiagnosticInterruptRequest(BaseModel):
    InstanceId: StrictStr
    DryRun: StrictBool | None = None
