from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDescribePredefinedAttributeRequest(BaseModel):
    InstanceId: StrictStr
    Name: StrictStr
