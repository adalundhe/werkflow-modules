from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteFlowLogsRequest(BaseModel):
    FlowLogIds: list[StrictStr]
    DryRun: StrictBool | None = None
