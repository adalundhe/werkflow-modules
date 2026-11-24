from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class ComputeOptimizerRDSDatabaseProjectedMetric(BaseModel):
    name: StrictStr | None = None
    timestamps: list[datetime.datetime | StrictStr] | None = None
    values: list[StrictFloat | StrictInt] | None = None
