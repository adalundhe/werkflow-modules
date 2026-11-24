from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailDashboardDetail(BaseModel):
    DashboardArn: StrictStr | None = None
    Type: StrictStr | None = None
