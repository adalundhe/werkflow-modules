from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDeletePredefinedAttributeRequest(BaseModel):
    InstanceId: StrictStr
    Name: StrictStr
