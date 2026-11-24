from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DevOpsGuruDescribeAccountOverviewRequest(BaseModel):
    FromTime: datetime.datetime | StrictStr
    ToTime: datetime.datetime | StrictStr | None = None
