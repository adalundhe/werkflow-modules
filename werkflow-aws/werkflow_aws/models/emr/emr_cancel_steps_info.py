from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRCancelStepsInfo(BaseModel):
    StepId: StrictStr | None = None
    Status: StrictStr | None = None
    Reason: StrictStr | None = None
