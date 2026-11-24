from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SchedulerListSchedulesRequest(BaseModel):
    GroupName: StrictStr | None = None
    NamePrefix: StrictStr | None = None
    State: Literal['ENABLED', 'DISABLED'] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
