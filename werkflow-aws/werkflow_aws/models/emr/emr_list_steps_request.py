from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EMRListStepsRequest(BaseModel):
    ClusterId: StrictStr
    StepStates: list[Literal['PENDING', 'CANCEL_PENDING', 'RUNNING', 'COMPLETED', 'CANCELLED', 'FAILED', 'INTERRUPTED']] | None = None
    StepIds: list[StrictStr] | None = None
    Marker: StrictStr | None = None
