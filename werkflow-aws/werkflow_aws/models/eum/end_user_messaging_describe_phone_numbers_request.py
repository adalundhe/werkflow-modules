from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .end_user_messaging_phone_number_filter import EndUserMessagingPhoneNumberFilter


class EndUserMessagingDescribePhoneNumbersRequest(BaseModel):
    PhoneNumberIds: list[StrictStr] | None = None
    Filters: list[EndUserMessagingPhoneNumberFilter] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    Owner: Literal['SELF', 'SHARED'] | None = None
