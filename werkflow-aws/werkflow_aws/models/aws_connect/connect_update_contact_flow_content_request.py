from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectUpdateContactFlowContentRequest(BaseModel):
    InstanceId: StrictStr
    ContactFlowId: StrictStr
    Content: StrictStr
