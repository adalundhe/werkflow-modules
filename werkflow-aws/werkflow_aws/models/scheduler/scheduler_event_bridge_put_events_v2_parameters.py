from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SchedulerEventBridgePutEventsV2Parameters(BaseModel):
    DetailType: StrictStr | None = None
    Source: StrictStr | None = None
