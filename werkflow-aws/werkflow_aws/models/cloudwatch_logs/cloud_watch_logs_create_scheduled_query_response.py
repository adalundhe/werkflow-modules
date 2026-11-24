from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CloudWatchLogsCreateScheduledQueryResponse(BaseModel):
    scheduledQueryArn: StrictStr | None = None
    state: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
