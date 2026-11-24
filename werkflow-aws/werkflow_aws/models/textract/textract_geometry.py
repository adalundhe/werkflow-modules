from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .textract_bounding_box import TextractBoundingBox
from .textract_point import TextractPoint


class TextractGeometry(BaseModel):
    BoundingBox: TextractBoundingBox | None = None
    Polygon: list[TextractPoint] | None = None
    RotationAngle: StrictFloat | StrictInt | None = None
