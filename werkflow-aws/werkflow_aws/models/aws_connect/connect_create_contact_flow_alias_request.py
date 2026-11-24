from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectCreateContactFlowAliasRequest(BaseModel):
    InstanceId: StrictStr
    ContactFlowId: StrictStr
    ContactFlowVersion: StrictInt
    AliasName: StrictStr
    Description: StrictStr | None = None
