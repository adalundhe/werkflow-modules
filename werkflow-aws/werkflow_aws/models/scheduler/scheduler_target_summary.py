from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SchedulerTargetSummary(BaseModel):
    Arn: StrictStr | None = None
