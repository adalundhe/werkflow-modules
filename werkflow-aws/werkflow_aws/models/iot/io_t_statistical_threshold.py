from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTStatisticalThreshold(BaseModel):
    statistic: StrictStr | None = None
