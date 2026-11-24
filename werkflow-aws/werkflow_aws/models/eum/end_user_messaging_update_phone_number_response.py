from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class EndUserMessagingUpdatePhoneNumberResponse(BaseModel):
    PhoneNumberArn: StrictStr | None = None
    PhoneNumberId: StrictStr | None = None
    PhoneNumber: StrictStr | None = None
    Status: StrictStr | None = None
    IsoCountryCode: StrictStr | None = None
    MessageType: StrictStr | None = None
    NumberCapabilities: list[StrictStr] | None = None
    NumberType: StrictStr | None = None
    MonthlyLeasingPrice: StrictStr | None = None
    TwoWayEnabled: StrictBool | None = None
    TwoWayChannelArn: StrictStr | None = None
    TwoWayChannelRole: StrictStr | None = None
    SelfManagedOptOutsEnabled: StrictBool | None = None
    OptOutListName: StrictStr | None = None
    InternationalSendingEnabled: StrictBool | None = None
    DeletionProtectionEnabled: StrictBool | None = None
    RegistrationId: StrictStr | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
