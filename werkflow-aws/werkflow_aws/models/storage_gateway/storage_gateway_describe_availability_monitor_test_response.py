from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class StorageGatewayDescribeAvailabilityMonitorTestResponse(BaseModel):
    GatewayARN: StrictStr | None = None
    Status: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
