from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_notification_recipient_type import ConnectNotificationRecipientType


class ConnectSendNotificationActionDefinition(BaseModel):
    DeliveryMethod: StrictStr | None = None
    Subject: StrictStr | None = None
    Content: StrictStr | None = None
    ContentType: StrictStr | None = None
    Recipient: ConnectNotificationRecipientType | None = None
    Exclusion: ConnectNotificationRecipientType | None = None
