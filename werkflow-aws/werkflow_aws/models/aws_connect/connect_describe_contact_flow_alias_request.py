from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDescribeContactFlowAliasRequest(BaseModel):
    InstanceId: StrictStr
    ContactFlowId: StrictStr
    AliasId: StrictStr
