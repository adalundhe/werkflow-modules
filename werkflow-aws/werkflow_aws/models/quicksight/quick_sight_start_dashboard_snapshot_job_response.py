from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightStartDashboardSnapshotJobResponse(BaseModel):
    Arn: StrictStr | None = None
    SnapshotJobId: StrictStr | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
