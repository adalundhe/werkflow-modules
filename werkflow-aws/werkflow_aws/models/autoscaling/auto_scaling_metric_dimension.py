from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingMetricDimension(BaseModel):
    Name: StrictStr | None = None
    Value: StrictStr | None = None
