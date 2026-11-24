from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EC2ApplicationStatusSummary(BaseModel):
    Status: StrictStr | None = None
    ImpairedSince: datetime.datetime | StrictStr | None = None
