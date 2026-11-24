from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class ComputeOptimizerECSServiceProjectedMetric(BaseModel):
    name: StrictStr | None = None
    timestamps: list[datetime.datetime | StrictStr] | None = None
    upperBoundValues: list[StrictFloat | StrictInt] | None = None
    lowerBoundValues: list[StrictFloat | StrictInt] | None = None
