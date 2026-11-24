from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LightsailLogEvent(BaseModel):
    createdAt: datetime.datetime | StrictStr | None = None
    message: StrictStr | None = None
