from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchListDashboardsRequest(BaseModel):
    DashboardNamePrefix: StrictStr | None = None
    NextToken: StrictStr | None = None
