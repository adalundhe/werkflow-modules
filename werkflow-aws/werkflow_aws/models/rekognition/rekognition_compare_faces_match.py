from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .rekognition_compared_face import RekognitionComparedFace


class RekognitionCompareFacesMatch(BaseModel):
    Similarity: StrictFloat | StrictInt | None = None
    Face: RekognitionComparedFace | None = None
