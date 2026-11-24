from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectListPhoneNumbersSummary(BaseModel):
    PhoneNumberId: StrictStr | None = None
    PhoneNumberArn: StrictStr | None = None
    PhoneNumber: StrictStr | None = None
    PhoneNumberCountryCode: StrictStr | None = None
    PhoneNumberType: StrictStr | None = None
    TargetArn: StrictStr | None = None
    InstanceId: StrictStr | None = None
    PhoneNumberDescription: StrictStr | None = None
    SourcePhoneNumberArn: StrictStr | None = None
