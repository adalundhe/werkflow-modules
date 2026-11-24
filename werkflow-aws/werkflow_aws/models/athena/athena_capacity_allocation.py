from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AthenaCapacityAllocation(BaseModel):
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    RequestTime: datetime.datetime | StrictStr | None = None
    RequestCompletionTime: datetime.datetime | StrictStr | None = None
