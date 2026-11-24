from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StepFunctionsStopExecutionRequest(BaseModel):
    executionArn: StrictStr
    error: StrictStr | None = None
    cause: StrictStr | None = None
