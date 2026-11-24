from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DevOpsGuruNotificationFilterConfig(BaseModel):
    Severities: list[StrictStr] | None = None
    MessageTypes: list[StrictStr] | None = None
