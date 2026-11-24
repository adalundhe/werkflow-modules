from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRTerminateJobFlowsRequest(BaseModel):
    JobFlowIds: list[StrictStr]
