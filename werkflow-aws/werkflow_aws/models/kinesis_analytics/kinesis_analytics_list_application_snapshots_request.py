from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KinesisAnalyticsListApplicationSnapshotsRequest(BaseModel):
    ApplicationName: StrictStr
    Limit: StrictInt | None = None
    NextToken: StrictStr | None = None
