from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .end_user_messaging_number_preference_item import EndUserMessagingNumberPreferenceItem


class EndUserMessagingListAvailablePhoneNumbersRequest(BaseModel):
    IsoCountryCode: StrictStr
    NumberCapabilities: list[Literal['SMS', 'VOICE', 'MMS', 'RCS']]
    NumberType: Literal['TEN_DLC']
    RegistrationId: StrictStr | None = None
    NumberPreference: list[EndUserMessagingNumberPreferenceItem] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
