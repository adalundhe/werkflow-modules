from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .rekognition_face_match import RekognitionFaceMatch
from .rekognition_person_detail import RekognitionPersonDetail


class RekognitionPersonMatch(BaseModel):
    Timestamp: StrictInt | None = None
    Person: RekognitionPersonDetail | None = None
    FaceMatches: list[RekognitionFaceMatch] | None = None
