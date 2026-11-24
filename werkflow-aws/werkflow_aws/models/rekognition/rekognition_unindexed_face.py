from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rekognition_face_detail import RekognitionFaceDetail


class RekognitionUnindexedFace(BaseModel):
    Reasons: list[StrictStr] | None = None
    FaceDetail: RekognitionFaceDetail | None = None
