from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .rekognition_bounding_box import RekognitionBoundingBox


class RekognitionFace(BaseModel):
    FaceId: StrictStr | None = None
    BoundingBox: RekognitionBoundingBox | None = None
    ImageId: StrictStr | None = None
    ExternalImageId: StrictStr | None = None
    Confidence: StrictFloat | StrictInt | None = None
    IndexFacesModelVersion: StrictStr | None = None
    UserId: StrictStr | None = None
