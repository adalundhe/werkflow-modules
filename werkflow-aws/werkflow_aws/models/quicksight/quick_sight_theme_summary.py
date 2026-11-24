from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightThemeSummary(BaseModel):
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    ThemeId: StrictStr | None = None
    LatestVersionNumber: StrictInt | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
