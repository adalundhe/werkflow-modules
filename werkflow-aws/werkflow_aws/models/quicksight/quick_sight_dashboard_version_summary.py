from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightDashboardVersionSummary(BaseModel):
    Arn: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    VersionNumber: StrictInt | None = None
    Status: StrictStr | None = None
    SourceEntityArn: StrictStr | None = None
    Description: StrictStr | None = None
