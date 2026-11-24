from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel
from .awss3_event_hold_duration_input import AWSS3EventHoldDurationInput


class AWSS3ObjectLockRetentionInput(BaseModel):
    Mode: Literal['GOVERNANCE', 'COMPLIANCE'] | None = None
    RetainUntilDate: datetime.datetime | str | None = None
    EventHold: Literal['ON', 'OFF'] | None = None
    EventHoldDuration: AWSS3EventHoldDurationInput | None = None
