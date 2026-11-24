from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_notification_resource import DataZoneNotificationResource


class DataZoneTopic(BaseModel):
    subject: StrictStr | None = None
    resource: DataZoneNotificationResource | None = None
    role: StrictStr | None = None
