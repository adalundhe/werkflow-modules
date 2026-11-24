from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2GetConsoleScreenshotRequest(BaseModel):
    InstanceId: StrictStr
    DryRun: StrictBool | None = None
    WakeUp: StrictBool | None = None
