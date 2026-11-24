from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectGetContactAttributesRequest(BaseModel):
    InstanceId: StrictStr
    InitialContactId: StrictStr
