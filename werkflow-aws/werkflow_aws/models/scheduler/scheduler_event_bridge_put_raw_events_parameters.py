from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SchedulerEventBridgePutRawEventsParameters(BaseModel):
    Metadata: dict[StrictStr, StrictStr] | None = None
