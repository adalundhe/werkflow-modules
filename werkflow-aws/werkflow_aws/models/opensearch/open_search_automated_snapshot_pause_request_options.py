from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class OpenSearchAutomatedSnapshotPauseRequestOptions(BaseModel):
    Enabled: StrictBool
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
