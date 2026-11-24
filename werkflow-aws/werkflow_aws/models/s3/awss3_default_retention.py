from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt
from .awss3_event_hold_duration import AWSS3EventHoldDuration


class AWSS3DefaultRetention(BaseModel):
    Mode: Literal['GOVERNANCE', 'COMPLIANCE'] | None = None
    Days: StrictInt | None = None
    Years: StrictInt | None = None
    DefaultEventHold: AWSS3EventHoldDuration | None = None
