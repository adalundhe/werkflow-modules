from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConnectUserNotificationSummary(BaseModel):
    NotificationId: StrictStr | None = None
    NotificationStatus: StrictStr | None = None
    InstanceId: StrictStr | None = None
    RecipientId: StrictStr | None = None
    Content: dict[StrictStr, StrictStr] | None = None
    Priority: StrictStr | None = None
    Source: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    ExpiresAt: datetime.datetime | StrictStr | None = None
