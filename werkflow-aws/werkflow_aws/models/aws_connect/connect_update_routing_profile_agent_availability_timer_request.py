from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectUpdateRoutingProfileAgentAvailabilityTimerRequest(BaseModel):
    InstanceId: StrictStr
    RoutingProfileId: StrictStr
    AgentAvailabilityTimer: Literal['TIME_SINCE_LAST_ACTIVITY', 'TIME_SINCE_LAST_INBOUND']
