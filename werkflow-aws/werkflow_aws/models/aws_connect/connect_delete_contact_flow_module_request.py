from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDeleteContactFlowModuleRequest(BaseModel):
    InstanceId: StrictStr
    ContactFlowModuleId: StrictStr
