from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDescribeContactFlowModuleAliasRequest(BaseModel):
    InstanceId: StrictStr
    ContactFlowModuleId: StrictStr
    AliasId: StrictStr
