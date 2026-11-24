from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class IoTJobSummary(BaseModel):
    jobArn: StrictStr | None = None
    jobId: StrictStr | None = None
    thingGroupId: StrictStr | None = None
    targetSelection: StrictStr | None = None
    status: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    lastUpdatedAt: datetime.datetime | StrictStr | None = None
    completedAt: datetime.datetime | StrictStr | None = None
    isConcurrent: StrictBool | None = None
