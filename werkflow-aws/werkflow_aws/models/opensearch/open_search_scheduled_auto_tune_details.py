from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class OpenSearchScheduledAutoTuneDetails(BaseModel):
    Date: datetime.datetime | StrictStr | None = None
    ActionType: StrictStr | None = None
    Action: StrictStr | None = None
    Severity: StrictStr | None = None
