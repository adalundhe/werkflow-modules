from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingVerifyDestinationNumberRequest(BaseModel):
    VerifiedDestinationNumberId: StrictStr
    VerificationCode: StrictStr
