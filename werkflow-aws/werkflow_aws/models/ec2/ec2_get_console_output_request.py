from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2GetConsoleOutputRequest(BaseModel):
    InstanceId: StrictStr
    Latest: StrictBool | None = None
    DryRun: StrictBool | None = None
