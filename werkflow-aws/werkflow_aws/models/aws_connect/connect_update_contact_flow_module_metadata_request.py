from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectUpdateContactFlowModuleMetadataRequest(BaseModel):
    InstanceId: StrictStr
    ContactFlowModuleId: StrictStr
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    State: Literal['ACTIVE', 'ARCHIVED'] | None = None
