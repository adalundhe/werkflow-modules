from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rekognition_celebrity import RekognitionCelebrity
from .rekognition_compared_face import RekognitionComparedFace


class RekognitionRecognizeCelebritiesResponse(BaseModel):
    CelebrityFaces: list[RekognitionCelebrity] | None = None
    UnrecognizedFaces: list[RekognitionComparedFace] | None = None
    OrientationCorrection: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
