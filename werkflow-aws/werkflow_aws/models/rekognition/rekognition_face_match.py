from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .rekognition_face import RekognitionFace


class RekognitionFaceMatch(BaseModel):
    Similarity: StrictFloat | StrictInt | None = None
    Face: RekognitionFace | None = None
