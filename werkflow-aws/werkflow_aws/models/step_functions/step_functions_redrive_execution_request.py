from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StepFunctionsRedriveExecutionRequest(BaseModel):
    executionArn: StrictStr
    clientToken: StrictStr | None = None
