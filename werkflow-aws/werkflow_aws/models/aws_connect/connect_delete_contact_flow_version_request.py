from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectDeleteContactFlowVersionRequest(BaseModel):
    InstanceId: StrictStr
    ContactFlowId: StrictStr
    ContactFlowVersion: StrictInt
