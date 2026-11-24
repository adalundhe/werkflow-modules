from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDeleteContactFlowModuleAliasRequest(BaseModel):
    InstanceId: StrictStr
    ContactFlowModuleId: StrictStr
    AliasId: StrictStr
