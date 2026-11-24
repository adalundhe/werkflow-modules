from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class StepFunctionsUpdateMapRunRequest(BaseModel):
    mapRunArn: StrictStr
    maxConcurrency: StrictInt | None = None
    toleratedFailurePercentage: StrictFloat | StrictInt | None = None
    toleratedFailureCount: StrictInt | None = None
