from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .macie_usage_total import MacieUsageTotal


class MacieGetUsageTotalsResponse(BaseModel):
    timeRange: StrictStr | None = None
    usageTotals: list[MacieUsageTotal] | None = None
    ResponseMetadata: dict[str, Any] | None = None
