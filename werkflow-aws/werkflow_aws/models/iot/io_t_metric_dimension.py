from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTMetricDimension(BaseModel):
    dimensionName: StrictStr | None = None
    operator: StrictStr | None = None
