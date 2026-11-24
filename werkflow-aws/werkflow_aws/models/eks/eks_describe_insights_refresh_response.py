from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class EKSDescribeInsightsRefreshResponse(BaseModel):
    message: StrictStr | None = None
    status: StrictStr | None = None
    startedAt: datetime.datetime | StrictStr | None = None
    endedAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
