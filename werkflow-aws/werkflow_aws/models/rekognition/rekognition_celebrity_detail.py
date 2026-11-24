from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .rekognition_bounding_box import RekognitionBoundingBox
from .rekognition_face_detail import RekognitionFaceDetail
from .rekognition_known_gender import RekognitionKnownGender


class RekognitionCelebrityDetail(BaseModel):
    Urls: list[StrictStr] | None = None
    Name: StrictStr | None = None
    Id: StrictStr | None = None
    Confidence: StrictFloat | StrictInt | None = None
    BoundingBox: RekognitionBoundingBox | None = None
    Face: RekognitionFaceDetail | None = None
    KnownGender: RekognitionKnownGender | None = None
