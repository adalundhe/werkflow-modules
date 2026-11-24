from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .rekognition_bounding_box import RekognitionBoundingBox
from .rekognition_face_match import RekognitionFaceMatch


class RekognitionSearchFacesByImageResponse(BaseModel):
    SearchedFaceBoundingBox: RekognitionBoundingBox | None = None
    SearchedFaceConfidence: StrictFloat | StrictInt | None = None
    FaceMatches: list[RekognitionFaceMatch] | None = None
    FaceModelVersion: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
