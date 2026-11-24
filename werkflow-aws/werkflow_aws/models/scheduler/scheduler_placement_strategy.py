from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SchedulerPlacementStrategy(BaseModel):
    type: StrictStr | None = None
    field: StrictStr | None = None
