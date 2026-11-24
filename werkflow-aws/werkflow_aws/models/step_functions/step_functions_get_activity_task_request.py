from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StepFunctionsGetActivityTaskRequest(BaseModel):
    activityArn: StrictStr
    workerName: StrictStr | None = None
