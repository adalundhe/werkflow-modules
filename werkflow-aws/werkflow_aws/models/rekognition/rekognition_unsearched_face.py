from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rekognition_face_detail import RekognitionFaceDetail


class RekognitionUnsearchedFace(BaseModel):
    FaceDetails: RekognitionFaceDetail | None = None
    Reasons: list[StrictStr] | None = None
