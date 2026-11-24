from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_dashboard import QuickSightDashboard


class QuickSightDescribeDashboardResponse(BaseModel):
    Dashboard: QuickSightDashboard | None = None
    Status: StrictInt | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
