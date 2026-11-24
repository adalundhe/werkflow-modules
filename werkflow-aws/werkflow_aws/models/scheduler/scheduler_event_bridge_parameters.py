from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SchedulerEventBridgeParameters(BaseModel):
    DetailType: StrictStr | None = None
    Source: StrictStr | None = None
