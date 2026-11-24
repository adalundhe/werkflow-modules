from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneNotificationConfig(BaseModel):
    notifyOn: list[StrictStr] | None = None
