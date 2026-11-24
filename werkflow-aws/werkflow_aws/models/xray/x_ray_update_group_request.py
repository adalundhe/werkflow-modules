from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .x_ray_insights_configuration import XRayInsightsConfiguration


class XRayUpdateGroupRequest(BaseModel):
    GroupName: StrictStr | None = None
    GroupARN: StrictStr | None = None
    FilterExpression: StrictStr | None = None
    InsightsConfiguration: XRayInsightsConfiguration | None = None
