from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .x_ray_anomalous_service import XRayAnomalousService
from .x_ray_request_impact_statistics import XRayRequestImpactStatistics


class XRayInsightEvent(BaseModel):
    Summary: StrictStr | None = None
    EventTime: datetime.datetime | StrictStr | None = None
    ClientRequestImpactStatistics: XRayRequestImpactStatistics | None = None
    RootCauseServiceRequestImpactStatistics: XRayRequestImpactStatistics | None = None
    TopAnomalousServices: list[XRayAnomalousService] | None = None
