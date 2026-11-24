from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDeleteEmailAddressRequest(BaseModel):
    InstanceId: StrictStr
    EmailAddressId: StrictStr
