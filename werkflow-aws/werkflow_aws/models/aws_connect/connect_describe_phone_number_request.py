from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDescribePhoneNumberRequest(BaseModel):
    PhoneNumberId: StrictStr
