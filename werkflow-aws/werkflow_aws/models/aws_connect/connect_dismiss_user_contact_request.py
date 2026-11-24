from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDismissUserContactRequest(BaseModel):
    UserId: StrictStr
    InstanceId: StrictStr
    ContactId: StrictStr
