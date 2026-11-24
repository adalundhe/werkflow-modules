from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CloudWatchGetDashboardResponse(BaseModel):
    DashboardArn: StrictStr | None = None
    DashboardBody: StrictStr | None = None
    DashboardName: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
