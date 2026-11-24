from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectPutUserStatusRequest(BaseModel):
    UserId: StrictStr
    InstanceId: StrictStr
    AgentStatusId: StrictStr
