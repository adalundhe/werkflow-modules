from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class QuickSightAppSummary(BaseModel):
    AppId: StrictStr | None = None
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    Visibility: StrictStr | None = None
