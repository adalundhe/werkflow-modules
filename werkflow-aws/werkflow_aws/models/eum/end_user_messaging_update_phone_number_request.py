from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EndUserMessagingUpdatePhoneNumberRequest(BaseModel):
    PhoneNumberId: StrictStr
    TwoWayEnabled: StrictBool | None = None
    TwoWayChannelArn: StrictStr | None = None
    TwoWayChannelRole: StrictStr | None = None
    SelfManagedOptOutsEnabled: StrictBool | None = None
    OptOutListName: StrictStr | None = None
    InternationalSendingEnabled: StrictBool | None = None
    DeletionProtectionEnabled: StrictBool | None = None
