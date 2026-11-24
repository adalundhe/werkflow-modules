from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class ComputeOptimizerIdleSummary(BaseModel):
    name: StrictStr | None = None
    value: StrictFloat | StrictInt | None = None
