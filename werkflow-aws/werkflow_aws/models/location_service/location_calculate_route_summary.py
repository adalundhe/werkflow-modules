from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class LocationCalculateRouteSummary(BaseModel):
    RouteBBox: list[StrictFloat | StrictInt] | None = None
    DataSource: StrictStr | None = None
    Distance: StrictFloat | StrictInt | None = None
    DurationSeconds: StrictFloat | StrictInt | None = None
    DistanceUnit: StrictStr | None = None
