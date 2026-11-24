from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class ConnectMetricFilterNumberCondition(BaseModel):
    Comparison: StrictStr | None = None
    Values: list[StrictFloat | StrictInt] | None = None
