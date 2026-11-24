from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .quick_sight_dashboard_version import QuickSightDashboardVersion


class QuickSightDashboard(BaseModel):
    DashboardId: StrictStr | None = None
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    Version: QuickSightDashboardVersion | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastPublishedTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    LinkEntities: list[StrictStr] | None = None
