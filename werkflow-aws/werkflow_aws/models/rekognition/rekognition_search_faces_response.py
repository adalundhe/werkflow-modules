from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rekognition_face_match import RekognitionFaceMatch


class RekognitionSearchFacesResponse(BaseModel):
    SearchedFaceId: StrictStr | None = None
    FaceMatches: list[RekognitionFaceMatch] | None = None
    FaceModelVersion: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
