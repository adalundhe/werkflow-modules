from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectUpdateContactFlowModuleAliasRequest(BaseModel):
    InstanceId: StrictStr
    ContactFlowModuleId: StrictStr
    AliasId: StrictStr
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    ContactFlowModuleVersion: StrictInt | None = None
