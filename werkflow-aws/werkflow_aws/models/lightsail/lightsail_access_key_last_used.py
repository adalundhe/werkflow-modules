from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LightsailAccessKeyLastUsed(BaseModel):
    lastUsedDate: datetime.datetime | StrictStr | None = None
    region: StrictStr | None = None
    serviceName: StrictStr | None = None
