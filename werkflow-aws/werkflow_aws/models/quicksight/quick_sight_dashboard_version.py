from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_dashboard_error import QuickSightDashboardError
from .quick_sight_sheet import QuickSightSheet


class QuickSightDashboardVersion(BaseModel):
    CreatedTime: datetime.datetime | StrictStr | None = None
    Errors: list[QuickSightDashboardError] | None = None
    VersionNumber: StrictInt | None = None
    Status: StrictStr | None = None
    Arn: StrictStr | None = None
    SourceEntityArn: StrictStr | None = None
    DataSetArns: list[StrictStr] | None = None
    TopicArns: list[StrictStr] | None = None
    Description: StrictStr | None = None
    ThemeArn: StrictStr | None = None
    Sheets: list[QuickSightSheet] | None = None
