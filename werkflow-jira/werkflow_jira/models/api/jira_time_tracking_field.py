from __future__ import annotations
from pydantic import BaseModel, StrictStr


class JiraTimeTrackingField(BaseModel):
    timeRemaining: StrictStr | None = None
