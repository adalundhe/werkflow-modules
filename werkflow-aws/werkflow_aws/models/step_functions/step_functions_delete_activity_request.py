from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StepFunctionsDeleteActivityRequest(BaseModel):
    activityArn: StrictStr
