from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class TimestreamQueryUpdateScheduledQueryRequest(BaseModel):
    ScheduledQueryArn: StrictStr
    State: Literal['ENABLED', 'DISABLED']
