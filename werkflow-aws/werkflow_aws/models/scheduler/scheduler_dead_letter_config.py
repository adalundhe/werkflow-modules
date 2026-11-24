from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SchedulerDeadLetterConfig(BaseModel):
    Arn: StrictStr | None = None
