from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConnectMetricSummary(BaseModel):
    Arn: StrictStr | None = None
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    Type: StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
