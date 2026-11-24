from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class PinpointNumberValidateResponse(BaseModel):
    Carrier: StrictStr | None = None
    City: StrictStr | None = None
    CleansedPhoneNumberE164: StrictStr | None = None
    CleansedPhoneNumberNational: StrictStr | None = None
    Country: StrictStr | None = None
    CountryCodeIso2: StrictStr | None = None
    CountryCodeNumeric: StrictStr | None = None
    County: StrictStr | None = None
    OriginalCountryCodeIso2: StrictStr | None = None
    OriginalPhoneNumber: StrictStr | None = None
    PhoneType: StrictStr | None = None
    PhoneTypeCode: StrictInt | None = None
    Timezone: StrictStr | None = None
    ZipCode: StrictStr | None = None
