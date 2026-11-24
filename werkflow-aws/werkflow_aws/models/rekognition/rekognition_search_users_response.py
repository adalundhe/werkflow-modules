from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rekognition_searched_face import RekognitionSearchedFace
from .rekognition_searched_user import RekognitionSearchedUser
from .rekognition_user_match import RekognitionUserMatch


class RekognitionSearchUsersResponse(BaseModel):
    UserMatches: list[RekognitionUserMatch] | None = None
    FaceModelVersion: StrictStr | None = None
    SearchedFace: RekognitionSearchedFace | None = None
    SearchedUser: RekognitionSearchedUser | None = None
    ResponseMetadata: dict[str, Any] | None = None
