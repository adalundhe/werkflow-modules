from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rekognition_searched_face_details import RekognitionSearchedFaceDetails
from .rekognition_unsearched_face import RekognitionUnsearchedFace
from .rekognition_user_match import RekognitionUserMatch


class RekognitionSearchUsersByImageResponse(BaseModel):
    UserMatches: list[RekognitionUserMatch] | None = None
    FaceModelVersion: StrictStr | None = None
    SearchedFace: RekognitionSearchedFaceDetails | None = None
    UnsearchedFaces: list[RekognitionUnsearchedFace] | None = None
    ResponseMetadata: dict[str, Any] | None = None
