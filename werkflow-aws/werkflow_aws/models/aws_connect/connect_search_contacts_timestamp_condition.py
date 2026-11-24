from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class ConnectSearchContactsTimestampCondition(BaseModel):
    Type: Literal['INITIATION_TIMESTAMP', 'SCHEDULED_TIMESTAMP', 'CONNECTED_TO_AGENT_TIMESTAMP', 'DISCONNECT_TIMESTAMP', 'ENQUEUE_TIMESTAMP']
    ConditionType: Literal['NOT_EXISTS']
