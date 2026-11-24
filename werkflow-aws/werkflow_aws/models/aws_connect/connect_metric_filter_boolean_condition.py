from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectMetricFilterBooleanCondition(BaseModel):
    Comparison: StrictStr | None = None
