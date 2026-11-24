from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightCreateDashboardResponse(BaseModel):
    Arn: StrictStr | None = None
    VersionArn: StrictStr | None = None
    DashboardId: StrictStr | None = None
    CreationStatus: StrictStr | None = None
    Status: StrictInt | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
