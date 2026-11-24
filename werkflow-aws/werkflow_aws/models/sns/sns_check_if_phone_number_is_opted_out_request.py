from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SNSCheckIfPhoneNumberIsOptedOutRequest(BaseModel):
    phoneNumber: StrictStr
