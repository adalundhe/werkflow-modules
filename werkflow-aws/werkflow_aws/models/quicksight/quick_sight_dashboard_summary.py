from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightDashboardSummary(BaseModel):
    Arn: StrictStr | None = None
    DashboardId: StrictStr | None = None
    Name: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    PublishedVersionNumber: StrictInt | None = None
    LastPublishedTime: datetime.datetime | StrictStr | None = None
