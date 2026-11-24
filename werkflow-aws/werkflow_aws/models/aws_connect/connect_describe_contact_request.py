from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDescribeContactRequest(BaseModel):
    InstanceId: StrictStr
    ContactId: StrictStr
