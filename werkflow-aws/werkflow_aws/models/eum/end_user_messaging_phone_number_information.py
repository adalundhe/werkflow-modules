from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .end_user_messaging_messaging_limits import EndUserMessagingMessagingLimits


class EndUserMessagingPhoneNumberInformation(BaseModel):
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
    PoolId: StrictStr | None = None
    RegistrationId: StrictStr | None = None
    MessagingLimits: EndUserMessagingMessagingLimits | None = None
    PricingTier: StrictStr | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
