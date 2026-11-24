from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectDeleteContactFlowModuleVersionRequest(BaseModel):
    InstanceId: StrictStr
    ContactFlowModuleId: StrictStr
    ContactFlowModuleVersion: StrictInt
