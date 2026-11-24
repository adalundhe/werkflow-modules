from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class QuickSightDataSourceSummary(BaseModel):
    Arn: StrictStr | None = None
    DataSourceId: StrictStr | None = None
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
