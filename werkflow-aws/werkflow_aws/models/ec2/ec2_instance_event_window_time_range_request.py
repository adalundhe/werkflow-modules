from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt


class EC2InstanceEventWindowTimeRangeRequest(BaseModel):
    StartWeekDay: Literal['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'] | None = None
    StartHour: StrictInt | None = None
    EndWeekDay: Literal['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'] | None = None
    EndHour: StrictInt | None = None
