from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class OpenSearchAutomatedSnapshotPauseOptions(BaseModel):
    Enabled: StrictBool | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    State: StrictStr | None = None
