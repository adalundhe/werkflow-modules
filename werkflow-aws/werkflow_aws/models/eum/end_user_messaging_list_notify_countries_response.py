from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .end_user_messaging_notify_country_information import EndUserMessagingNotifyCountryInformation


class EndUserMessagingListNotifyCountriesResponse(BaseModel):
    NotifyCountries: list[EndUserMessagingNotifyCountryInformation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
