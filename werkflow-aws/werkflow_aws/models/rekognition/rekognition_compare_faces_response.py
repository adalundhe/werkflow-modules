from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rekognition_compare_faces_match import RekognitionCompareFacesMatch
from .rekognition_compared_face import RekognitionComparedFace
from .rekognition_compared_source_image_face import RekognitionComparedSourceImageFace


class RekognitionCompareFacesResponse(BaseModel):
    SourceImageFace: RekognitionComparedSourceImageFace | None = None
    FaceMatches: list[RekognitionCompareFacesMatch] | None = None
    UnmatchedFaces: list[RekognitionComparedFace] | None = None
    SourceImageOrientationCorrection: StrictStr | None = None
    TargetImageOrientationCorrection: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
