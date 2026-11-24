from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDescribeContactFlowModuleRequest(BaseModel):
    InstanceId: StrictStr
    ContactFlowModuleId: StrictStr
