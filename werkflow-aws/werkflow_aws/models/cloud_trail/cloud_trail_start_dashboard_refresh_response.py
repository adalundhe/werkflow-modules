from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CloudTrailStartDashboardRefreshResponse(BaseModel):
    RefreshId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
