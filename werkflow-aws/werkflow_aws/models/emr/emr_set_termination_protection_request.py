from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EMRSetTerminationProtectionRequest(BaseModel):
    JobFlowIds: list[StrictStr]
    TerminationProtected: StrictBool
