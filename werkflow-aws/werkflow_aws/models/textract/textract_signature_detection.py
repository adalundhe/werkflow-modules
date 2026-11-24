from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .textract_geometry import TextractGeometry


class TextractSignatureDetection(BaseModel):
    Confidence: StrictFloat | StrictInt | None = None
    Geometry: TextractGeometry | None = None
