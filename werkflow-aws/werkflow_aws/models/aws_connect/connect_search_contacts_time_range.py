from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectSearchContactsTimeRange(BaseModel):
    Type: Literal['INITIATION_TIMESTAMP', 'SCHEDULED_TIMESTAMP', 'CONNECTED_TO_AGENT_TIMESTAMP', 'DISCONNECT_TIMESTAMP', 'ENQUEUE_TIMESTAMP']
    StartTime: datetime.datetime | StrictStr
    EndTime: datetime.datetime | StrictStr
