from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2ConnectionNotification(BaseModel):
    ConnectionNotificationId: StrictStr | None = None
    ServiceId: StrictStr | None = None
    VpcEndpointId: StrictStr | None = None
    ConnectionNotificationType: StrictStr | None = None
    ConnectionNotificationArn: StrictStr | None = None
    ConnectionEvents: list[StrictStr] | None = None
    ConnectionNotificationState: StrictStr | None = None
    ServiceRegion: StrictStr | None = None
