from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SNSOptInPhoneNumberRequest(BaseModel):
    phoneNumber: StrictStr
