from __future__ import annotations
from pydantic import BaseModel
from .comprehend_bounding_box import ComprehendBoundingBox
from .comprehend_point import ComprehendPoint


class ComprehendGeometry(BaseModel):
    BoundingBox: ComprehendBoundingBox | None = None
    Polygon: list[ComprehendPoint] | None = None
