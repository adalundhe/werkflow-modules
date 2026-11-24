from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_notification_recipient_type import ConnectNotificationRecipientType


class ConnectSendInAppNotificationActionDefinition(BaseModel):
    Content: dict[StrictStr, StrictStr] | None = None
    Recipient: ConnectNotificationRecipientType | None = None
    Exclusion: ConnectNotificationRecipientType | None = None
    Priority: StrictStr | None = None
