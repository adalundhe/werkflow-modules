from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StepFunctionsSendTaskFailureRequest(BaseModel):
    taskToken: StrictStr
    error: StrictStr | None = None
    cause: StrictStr | None = None
