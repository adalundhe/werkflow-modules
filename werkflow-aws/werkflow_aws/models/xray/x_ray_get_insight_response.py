from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .x_ray_insight import XRayInsight


class XRayGetInsightResponse(BaseModel):
    Insight: XRayInsight | None = None
    ResponseMetadata: dict[str, Any] | None = None
