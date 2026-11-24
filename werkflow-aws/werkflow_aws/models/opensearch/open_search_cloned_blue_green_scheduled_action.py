from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class OpenSearchClonedBlueGreenScheduledAction(BaseModel):
    Action: StrictStr | None = None
    ScheduledTime: datetime.datetime | StrictStr | None = None
