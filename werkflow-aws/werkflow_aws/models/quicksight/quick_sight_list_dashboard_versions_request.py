from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightListDashboardVersionsRequest(BaseModel):
    AwsAccountId: StrictStr
    DashboardId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
