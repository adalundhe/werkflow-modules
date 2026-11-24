from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .macie_usage_record import MacieUsageRecord


class MacieGetUsageStatisticsResponse(BaseModel):
    nextToken: StrictStr | None = None
    records: list[MacieUsageRecord] | None = None
    timeRange: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
