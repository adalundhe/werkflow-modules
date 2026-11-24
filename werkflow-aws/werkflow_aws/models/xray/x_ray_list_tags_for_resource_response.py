from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .x_ray_tag import XRayTag


class XRayListTagsForResourceResponse(BaseModel):
    Tags: list[XRayTag] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
