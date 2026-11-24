from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteFleetsRequest(BaseModel):
    FleetIds: list[StrictStr]
    TerminateInstances: StrictBool
    DryRun: StrictBool | None = None
