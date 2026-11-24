from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EMRSetUnhealthyNodeReplacementRequest(BaseModel):
    JobFlowIds: list[StrictStr]
    UnhealthyNodeReplacement: StrictBool
