from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectUpdateContactFlowNameRequest(BaseModel):
    InstanceId: StrictStr
    ContactFlowId: StrictStr
    Name: StrictStr | None = None
    Description: StrictStr | None = None
