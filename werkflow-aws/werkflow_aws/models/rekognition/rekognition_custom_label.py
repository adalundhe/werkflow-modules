from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .rekognition_geometry import RekognitionGeometry


class RekognitionCustomLabel(BaseModel):
    Name: StrictStr | None = None
    Confidence: StrictFloat | StrictInt | None = None
    Geometry: RekognitionGeometry | None = None
