from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .x_ray_insight_impact_graph_service import XRayInsightImpactGraphService


class XRayGetInsightImpactGraphResponse(BaseModel):
    InsightId: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    ServiceGraphStartTime: datetime.datetime | StrictStr | None = None
    ServiceGraphEndTime: datetime.datetime | StrictStr | None = None
    Services: list[XRayInsightImpactGraphService] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
