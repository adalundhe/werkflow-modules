from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_notification_property import GlueNotificationProperty


class GlueAction(BaseModel):
    JobName: StrictStr | None = None
    Arguments: dict[StrictStr, StrictStr] | None = None
    Timeout: StrictInt | None = None
    SecurityConfiguration: StrictStr | None = None
    NotificationProperty: GlueNotificationProperty | None = None
    CrawlerName: StrictStr | None = None
