from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel
from .awss3_event_hold_duration import AWSS3EventHoldDuration


class AWSS3ObjectLockRetention(BaseModel):
    Mode: Literal['GOVERNANCE', 'COMPLIANCE'] | None = None
    RetainUntilDate: datetime.datetime | None = None
    EventHold: Literal['ON', 'OFF'] | None = None
    EventHoldDuration: AWSS3EventHoldDuration | None = None
