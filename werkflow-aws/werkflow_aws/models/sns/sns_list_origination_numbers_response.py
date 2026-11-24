from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sns_phone_number_information import SNSPhoneNumberInformation


class SNSListOriginationNumbersResponse(BaseModel):
    NextToken: StrictStr | None = None
    PhoneNumbers: list[SNSPhoneNumberInformation] | None = None
    ResponseMetadata: dict[str, Any] | None = None
