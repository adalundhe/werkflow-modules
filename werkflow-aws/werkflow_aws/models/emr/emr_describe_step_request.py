from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRDescribeStepRequest(BaseModel):
    ClusterId: StrictStr
    StepId: StrictStr
