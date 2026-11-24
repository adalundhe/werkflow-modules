from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListAgentStatusesRequest(BaseModel):
    InstanceId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    AgentStatusTypes: list[Literal['ROUTABLE', 'CUSTOM', 'OFFLINE']] | None = None
