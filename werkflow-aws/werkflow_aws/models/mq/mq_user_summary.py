from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MQUserSummary(BaseModel):
    PendingChange: StrictStr | None = None
    Username: StrictStr | None = None
