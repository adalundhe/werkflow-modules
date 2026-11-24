from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_phone_number_status import ConnectPhoneNumberStatus


class ConnectClaimedPhoneNumberSummary(BaseModel):
    PhoneNumberId: StrictStr | None = None
    PhoneNumberArn: StrictStr | None = None
    PhoneNumber: StrictStr | None = None
    PhoneNumberCountryCode: StrictStr | None = None
    PhoneNumberType: StrictStr | None = None
    PhoneNumberDescription: StrictStr | None = None
    TargetArn: StrictStr | None = None
    InstanceId: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    PhoneNumberStatus: ConnectPhoneNumberStatus | None = None
    SourcePhoneNumberArn: StrictStr | None = None
