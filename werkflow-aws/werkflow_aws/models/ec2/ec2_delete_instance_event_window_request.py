from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteInstanceEventWindowRequest(BaseModel):
    InstanceEventWindowId: StrictStr
    DryRun: StrictBool | None = None
    ForceDelete: StrictBool | None = None
