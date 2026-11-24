from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .lightsail_access_key_last_used import LightsailAccessKeyLastUsed


class LightsailAccessKey(BaseModel):
    accessKeyId: StrictStr | None = None
    secretAccessKey: StrictStr | None = None
    status: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    lastUsed: LightsailAccessKeyLastUsed | None = None
