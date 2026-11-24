from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class OpenSearchChangeProgressDetails(BaseModel):
    ChangeId: StrictStr | None = None
    Message: StrictStr | None = None
    ConfigChangeStatus: StrictStr | None = None
    InitiatedBy: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
