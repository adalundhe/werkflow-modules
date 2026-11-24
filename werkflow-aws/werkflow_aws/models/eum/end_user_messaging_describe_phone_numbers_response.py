from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .end_user_messaging_phone_number_information import EndUserMessagingPhoneNumberInformation


class EndUserMessagingDescribePhoneNumbersResponse(BaseModel):
    PhoneNumbers: list[EndUserMessagingPhoneNumberInformation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
