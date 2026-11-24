from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieGetUsageTotalsRequest(BaseModel):
    timeRange: StrictStr | None = None
