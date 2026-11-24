from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .x_ray_insights_configuration import XRayInsightsConfiguration
from .x_ray_tag import XRayTag


class XRayCreateGroupRequest(BaseModel):
    GroupName: StrictStr
    FilterExpression: StrictStr | None = None
    InsightsConfiguration: XRayInsightsConfiguration | None = None
    Tags: list[XRayTag] | None = None
