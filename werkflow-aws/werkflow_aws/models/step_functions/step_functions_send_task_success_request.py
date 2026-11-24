from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StepFunctionsSendTaskSuccessRequest(BaseModel):
    taskToken: StrictStr
    output: StrictStr
