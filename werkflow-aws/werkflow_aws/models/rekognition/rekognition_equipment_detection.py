from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .rekognition_bounding_box import RekognitionBoundingBox
from .rekognition_covers_body_part import RekognitionCoversBodyPart


class RekognitionEquipmentDetection(BaseModel):
    BoundingBox: RekognitionBoundingBox | None = None
    Confidence: StrictFloat | StrictInt | None = None
    Type: StrictStr | None = None
    CoversBodyPart: RekognitionCoversBodyPart | None = None
