from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictStr
from .notification_recipients import NotificationRecipients
from .notification_recipients_restrictions import NotificationRecipientsRestrictions


class Notification(BaseModel):
    model_config = ConfigDict(extra="allow")

    htmlBody: StrictStr | None = None
    restrict: NotificationRecipientsRestrictions | None = None
    subject: StrictStr | None = None
    textBody: StrictStr | None = None
    to: NotificationRecipients | None = None
