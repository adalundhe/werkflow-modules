from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class ConnectUpdateAgentStatusRequest(BaseModel):
    InstanceId: StrictStr
    AgentStatusId: StrictStr
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    State: Literal['ENABLED', 'DISABLED'] | None = None
    DisplayOrder: StrictInt | None = None
    ResetOrderNumber: StrictBool | None = None
