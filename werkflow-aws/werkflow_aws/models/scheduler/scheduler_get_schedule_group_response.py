from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class SchedulerGetScheduleGroupResponse(BaseModel):
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    State: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    LastModificationDate: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
