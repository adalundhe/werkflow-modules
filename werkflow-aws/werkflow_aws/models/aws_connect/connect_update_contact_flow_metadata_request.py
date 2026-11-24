from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectUpdateContactFlowMetadataRequest(BaseModel):
    InstanceId: StrictStr
    ContactFlowId: StrictStr
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    ContactFlowState: Literal['ACTIVE', 'ARCHIVED'] | None = None
