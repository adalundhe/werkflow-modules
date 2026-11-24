from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LocationCalculateRouteMatrixSummary(BaseModel):
    DataSource: StrictStr | None = None
    RouteCount: StrictInt | None = None
    ErrorCount: StrictInt | None = None
    DistanceUnit: StrictStr | None = None
