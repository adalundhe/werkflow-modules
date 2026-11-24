from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt
from .awss3_event_hold_duration_input import AWSS3EventHoldDurationInput


class AWSS3DefaultRetentionInput(BaseModel):
    Mode: Literal['GOVERNANCE', 'COMPLIANCE'] | None = None
    Days: StrictInt | None = None
    Years: StrictInt | None = None
    DefaultEventHold: AWSS3EventHoldDurationInput | None = None
