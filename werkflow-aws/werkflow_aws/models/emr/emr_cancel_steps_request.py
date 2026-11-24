from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EMRCancelStepsRequest(BaseModel):
    ClusterId: StrictStr
    StepIds: list[StrictStr]
    StepCancellationOption: Literal['SEND_INTERRUPT', 'TERMINATE_PROCESS'] | None = None
