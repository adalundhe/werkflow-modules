from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightExcludePeriodConfiguration(BaseModel):
    Amount: StrictInt | None = None
    Granularity: StrictStr | None = None
    Status: StrictStr | None = None
