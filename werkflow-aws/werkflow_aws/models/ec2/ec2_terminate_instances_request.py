from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2TerminateInstancesRequest(BaseModel):
    InstanceIds: list[StrictStr]
    DryRun: StrictBool | None = None
