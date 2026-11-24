from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SchedulerSqsParameters(BaseModel):
    MessageGroupId: StrictStr | None = None
