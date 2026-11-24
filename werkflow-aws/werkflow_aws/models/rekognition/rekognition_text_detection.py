from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .rekognition_geometry import RekognitionGeometry


class RekognitionTextDetection(BaseModel):
    DetectedText: StrictStr | None = None
    Type: StrictStr | None = None
    Id: StrictInt | None = None
    ParentId: StrictInt | None = None
    Confidence: StrictFloat | StrictInt | None = None
    Geometry: RekognitionGeometry | None = None
