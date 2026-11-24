from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightUpdateDashboardLinksResponse(BaseModel):
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    DashboardArn: StrictStr | None = None
    LinkEntities: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
