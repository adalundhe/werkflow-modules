from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightDescribeDashboardRequest(BaseModel):
    AwsAccountId: StrictStr
    DashboardId: StrictStr
    VersionNumber: StrictInt | None = None
    AliasName: StrictStr | None = None
