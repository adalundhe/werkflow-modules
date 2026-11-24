from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .x_ray_anomalous_service import XRayAnomalousService
from .x_ray_request_impact_statistics import XRayRequestImpactStatistics
from .x_ray_service_id import XRayServiceId


class XRayInsightSummary(BaseModel):
    InsightId: StrictStr | None = None
    GroupARN: StrictStr | None = None
    GroupName: StrictStr | None = None
    RootCauseServiceId: XRayServiceId | None = None
    Categories: list[StrictStr] | None = None
    State: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    Summary: StrictStr | None = None
    ClientRequestImpactStatistics: XRayRequestImpactStatistics | None = None
    RootCauseServiceRequestImpactStatistics: XRayRequestImpactStatistics | None = None
    TopAnomalousServices: list[XRayAnomalousService] | None = None
    LastUpdateTime: datetime.datetime | StrictStr | None = None
