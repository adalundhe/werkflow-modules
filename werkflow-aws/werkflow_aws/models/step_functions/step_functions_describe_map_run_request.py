from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StepFunctionsDescribeMapRunRequest(BaseModel):
    mapRunArn: StrictStr
