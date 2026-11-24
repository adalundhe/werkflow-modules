from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectUpdateUserNotificationStatusRequest(BaseModel):
    InstanceId: StrictStr
    NotificationId: StrictStr
    UserId: StrictStr
    Status: Literal['READ', 'UNREAD', 'HIDDEN']
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
