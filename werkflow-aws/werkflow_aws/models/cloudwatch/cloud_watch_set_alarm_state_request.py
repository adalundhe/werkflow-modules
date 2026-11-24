from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CloudWatchSetAlarmStateRequest(BaseModel):
    AlarmName: StrictStr
    StateValue: Literal['OK', 'ALARM', 'INSUFFICIENT_DATA']
    StateReason: StrictStr
    StateReasonData: StrictStr | None = None
