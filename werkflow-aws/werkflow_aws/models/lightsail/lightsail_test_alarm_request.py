from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class LightsailTestAlarmRequest(BaseModel):
    alarmName: StrictStr
    state: Literal['OK', 'ALARM', 'INSUFFICIENT_DATA']
