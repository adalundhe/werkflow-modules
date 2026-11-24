from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightThemeVersionSummary(BaseModel):
    VersionNumber: StrictInt | None = None
    Arn: StrictStr | None = None
    Description: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
