from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectPhoneNumberSummary(BaseModel):
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    PhoneNumber: StrictStr | None = None
    PhoneNumberType: StrictStr | None = None
    PhoneNumberCountryCode: StrictStr | None = None
