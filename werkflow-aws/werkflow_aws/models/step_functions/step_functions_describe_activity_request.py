from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StepFunctionsDescribeActivityRequest(BaseModel):
    activityArn: StrictStr
