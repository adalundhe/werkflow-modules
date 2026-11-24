from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectUpdateContactAttributesRequest(BaseModel):
    InitialContactId: StrictStr
    InstanceId: StrictStr
    Attributes: dict[StrictStr, StrictStr]
