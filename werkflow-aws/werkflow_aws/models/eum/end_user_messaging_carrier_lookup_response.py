from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class EndUserMessagingCarrierLookupResponse(BaseModel):
    E164PhoneNumber: StrictStr | None = None
    DialingCountryCode: StrictStr | None = None
    IsoCountryCode: StrictStr | None = None
    Country: StrictStr | None = None
    MCC: StrictStr | None = None
    MNC: StrictStr | None = None
    Carrier: StrictStr | None = None
    PhoneNumberType: StrictStr | None = None
    OriginalPhoneNumber: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
