from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KinesisAnalyticsListApplicationsRequest(BaseModel):
    Limit: StrictInt | None = None
    NextToken: StrictStr | None = None
