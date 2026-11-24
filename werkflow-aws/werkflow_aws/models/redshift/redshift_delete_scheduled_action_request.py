from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftDeleteScheduledActionRequest(BaseModel):
    ScheduledActionName: StrictStr
