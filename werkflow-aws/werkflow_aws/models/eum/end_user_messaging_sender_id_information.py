from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .end_user_messaging_messaging_limits import EndUserMessagingMessagingLimits


class EndUserMessagingSenderIdInformation(BaseModel):
    SenderIdArn: StrictStr | None = None
    SenderId: StrictStr | None = None
    IsoCountryCode: StrictStr | None = None
    MessageTypes: list[StrictStr] | None = None
    MonthlyLeasingPrice: StrictStr | None = None
    DeletionProtectionEnabled: StrictBool | None = None
    Registered: StrictBool | None = None
    RegistrationId: StrictStr | None = None
    MessagingLimits: EndUserMessagingMessagingLimits | None = None
    PricingTier: StrictStr | None = None
