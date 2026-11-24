from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StepFunctionsActivityScheduleFailedEventDetails(BaseModel):
    error: StrictStr | None = None
    cause: StrictStr | None = None
