from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class PinpointMetricDimension(BaseModel):
    ComparisonOperator: StrictStr | None = None
    Value: StrictFloat | StrictInt | None = None
