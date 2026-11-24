from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDescribeContactFlowRequest(BaseModel):
    InstanceId: StrictStr
    ContactFlowId: StrictStr
