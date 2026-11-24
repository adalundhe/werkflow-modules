from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectCreateAgentStatusRequest(BaseModel):
    InstanceId: StrictStr
    Name: StrictStr
    State: Literal['ENABLED', 'DISABLED']
    Description: StrictStr | None = None
    DisplayOrder: StrictInt | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
