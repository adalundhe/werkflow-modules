from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StepFunctionsStartExecutionRequest(BaseModel):
    stateMachineArn: StrictStr
    name: StrictStr | None = None
    input: StrictStr | None = None
    traceHeader: StrictStr | None = None
