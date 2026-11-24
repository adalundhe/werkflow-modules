from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectNotificationRecipientType(BaseModel):
    UserTags: dict[StrictStr, StrictStr] | None = None
    UserIds: list[StrictStr] | None = None
