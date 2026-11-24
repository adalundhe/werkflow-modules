from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightCreateRefreshScheduleResponse(BaseModel):
    Status: StrictInt | None = None
    RequestId: StrictStr | None = None
    ScheduleId: StrictStr | None = None
    Arn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
