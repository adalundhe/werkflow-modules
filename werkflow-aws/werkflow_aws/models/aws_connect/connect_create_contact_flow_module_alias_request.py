from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectCreateContactFlowModuleAliasRequest(BaseModel):
    InstanceId: StrictStr
    ContactFlowModuleId: StrictStr
    ContactFlowModuleVersion: StrictInt
    AliasName: StrictStr
    Description: StrictStr | None = None
