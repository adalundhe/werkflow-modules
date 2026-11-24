from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SNSPhoneNumberInformation(BaseModel):
    CreatedAt: datetime.datetime | StrictStr | None = None
    PhoneNumber: StrictStr | None = None
    Status: StrictStr | None = None
    Iso2CountryCode: StrictStr | None = None
    RouteType: StrictStr | None = None
    NumberCapabilities: list[StrictStr] | None = None
