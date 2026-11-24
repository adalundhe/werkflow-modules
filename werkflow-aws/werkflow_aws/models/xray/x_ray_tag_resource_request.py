from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .x_ray_tag import XRayTag


class XRayTagResourceRequest(BaseModel):
    ResourceARN: StrictStr
    Tags: list[XRayTag]
