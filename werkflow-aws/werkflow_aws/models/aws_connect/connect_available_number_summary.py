from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectAvailableNumberSummary(BaseModel):
    PhoneNumber: StrictStr | None = None
    PhoneNumberCountryCode: StrictStr | None = None
    PhoneNumberType: StrictStr | None = None
