from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDescribeEmailAddressRequest(BaseModel):
    InstanceId: StrictStr
    EmailAddressId: StrictStr
