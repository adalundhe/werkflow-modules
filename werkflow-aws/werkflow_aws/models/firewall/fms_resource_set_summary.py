from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class FMSResourceSetSummary(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    LastUpdateTime: datetime.datetime | StrictStr | None = None
    ResourceSetStatus: StrictStr | None = None
