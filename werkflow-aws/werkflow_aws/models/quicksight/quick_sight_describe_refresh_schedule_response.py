from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_refresh_schedule import QuickSightRefreshSchedule


class QuickSightDescribeRefreshScheduleResponse(BaseModel):
    RefreshSchedule: QuickSightRefreshSchedule | None = None
    Status: StrictInt | None = None
    RequestId: StrictStr | None = None
    Arn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
