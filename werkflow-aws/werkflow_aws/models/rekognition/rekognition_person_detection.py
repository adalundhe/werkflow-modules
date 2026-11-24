from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .rekognition_person_detail import RekognitionPersonDetail


class RekognitionPersonDetection(BaseModel):
    Timestamp: StrictInt | None = None
    Person: RekognitionPersonDetail | None = None
