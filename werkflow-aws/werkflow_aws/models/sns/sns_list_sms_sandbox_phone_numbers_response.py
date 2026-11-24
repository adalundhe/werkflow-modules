from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .snssms_sandbox_phone_number import SNSSMSSandboxPhoneNumber


class SNSListSMSSandboxPhoneNumbersResponse(BaseModel):
    PhoneNumbers: list[SNSSMSSandboxPhoneNumber] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
