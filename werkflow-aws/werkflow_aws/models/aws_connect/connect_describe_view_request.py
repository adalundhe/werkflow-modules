from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDescribeViewRequest(BaseModel):
    InstanceId: StrictStr
    ViewId: StrictStr
