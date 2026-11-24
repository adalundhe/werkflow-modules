from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2StopInstancesRequest(BaseModel):
    InstanceIds: list[StrictStr]
    Hibernate: StrictBool | None = None
    Force: StrictBool | None = None
    DryRun: StrictBool | None = None
