from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudTrailDescribeTrailsRequest(BaseModel):
    trailNameList: list[StrictStr] | None = None
    includeShadowTrails: StrictBool | None = None
