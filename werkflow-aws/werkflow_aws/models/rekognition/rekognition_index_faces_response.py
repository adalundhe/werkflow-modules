from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rekognition_face_record import RekognitionFaceRecord
from .rekognition_unindexed_face import RekognitionUnindexedFace


class RekognitionIndexFacesResponse(BaseModel):
    FaceRecords: list[RekognitionFaceRecord] | None = None
    OrientationCorrection: StrictStr | None = None
    FaceModelVersion: StrictStr | None = None
    UnindexedFaces: list[RekognitionUnindexedFace] | None = None
    ResponseMetadata: dict[str, Any] | None = None
