from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchDashboardEntry(BaseModel):
    DashboardName: StrictStr | None = None
    DashboardArn: StrictStr | None = None
    LastModified: datetime.datetime | StrictStr | None = None
    Size: StrictInt | None = None
