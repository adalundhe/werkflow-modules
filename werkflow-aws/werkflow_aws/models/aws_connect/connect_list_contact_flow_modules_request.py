from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListContactFlowModulesRequest(BaseModel):
    InstanceId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    ContactFlowModuleState: Literal['ACTIVE', 'ARCHIVED'] | None = None
