from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectUpdateContactFlowAliasRequest(BaseModel):
    InstanceId: StrictStr
    ContactFlowId: StrictStr
    AliasId: StrictStr
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    ContactFlowVersion: StrictInt | None = None
