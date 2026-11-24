from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .end_user_messaging_carrier_status_information import EndUserMessagingCarrierStatusInformation


class EndUserMessagingCountryLaunchStatusInformation(BaseModel):
    IsoCountryCode: StrictStr | None = None
    Status: StrictStr | None = None
    RcsPlatformId: StrictStr | None = None
    RegistrationId: StrictStr | None = None
    CarrierStatus: list[EndUserMessagingCarrierStatusInformation] | None = None
