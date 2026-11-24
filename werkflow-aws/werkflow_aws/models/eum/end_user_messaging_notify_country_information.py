from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EndUserMessagingNotifyCountryInformation(BaseModel):
    IsoCountryCode: StrictStr | None = None
    CountryName: StrictStr | None = None
    SupportedChannels: list[StrictStr] | None = None
    SupportedUseCases: list[StrictStr] | None = None
    SupportedTiers: list[StrictStr] | None = None
    CustomerOwnedIdentityRequired: StrictBool | None = None
