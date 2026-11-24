from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SSMParentStepDetails(BaseModel):
    StepExecutionId: StrictStr | None = None
    StepName: StrictStr | None = None
    Action: StrictStr | None = None
    Iteration: StrictInt | None = None
    IteratorValue: StrictStr | None = None
