from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rekognition_face_detail import RekognitionFaceDetail


class RekognitionDetectFacesResponse(BaseModel):
    FaceDetails: list[RekognitionFaceDetail] | None = None
    OrientationCorrection: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
