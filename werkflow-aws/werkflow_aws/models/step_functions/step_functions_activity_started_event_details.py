from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StepFunctionsActivityStartedEventDetails(BaseModel):
    workerName: StrictStr | None = None
