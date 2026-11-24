from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rekognition_face import RekognitionFace


class RekognitionListFacesResponse(BaseModel):
    Faces: list[RekognitionFace] | None = None
    NextToken: StrictStr | None = None
    FaceModelVersion: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
