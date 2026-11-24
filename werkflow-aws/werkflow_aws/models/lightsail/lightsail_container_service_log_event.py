from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LightsailContainerServiceLogEvent(BaseModel):
    createdAt: datetime.datetime | StrictStr | None = None
    message: StrictStr | None = None
