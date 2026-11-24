from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ECSManagedAgent(BaseModel):
    lastStartedAt: datetime.datetime | StrictStr | None = None
    name: StrictStr | None = None
    reason: StrictStr | None = None
    lastStatus: StrictStr | None = None
