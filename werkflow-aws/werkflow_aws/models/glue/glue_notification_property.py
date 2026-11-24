from __future__ import annotations
from pydantic import BaseModel, StrictInt


class GlueNotificationProperty(BaseModel):
    NotifyDelayAfter: StrictInt | None = None
