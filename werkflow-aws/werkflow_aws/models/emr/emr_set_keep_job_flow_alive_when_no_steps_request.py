from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EMRSetKeepJobFlowAliveWhenNoStepsRequest(BaseModel):
    JobFlowIds: list[StrictStr]
    KeepJobFlowAliveWhenNoSteps: StrictBool
