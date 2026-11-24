from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SchedulerListScheduleGroupsRequest(BaseModel):
    NamePrefix: StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
