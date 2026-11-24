from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectAssociateContactWithUserRequest(BaseModel):
    InstanceId: StrictStr
    ContactId: StrictStr
    UserId: StrictStr
