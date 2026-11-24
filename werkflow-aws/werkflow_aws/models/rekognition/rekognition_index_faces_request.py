from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .rekognition_image import RekognitionImage


class RekognitionIndexFacesRequest(BaseModel):
    CollectionId: StrictStr
    Image: RekognitionImage
    ExternalImageId: StrictStr | None = None
    DetectionAttributes: list[Literal['DEFAULT', 'ALL', 'AGE_RANGE', 'BEARD', 'EMOTIONS', 'EYE_DIRECTION', 'EYEGLASSES', 'EYES_OPEN', 'GENDER', 'MOUTH_OPEN', 'MUSTACHE', 'FACE_OCCLUDED', 'SMILE', 'SUNGLASSES']] | None = None
    MaxFaces: StrictInt | None = None
    QualityFilter: Literal['NONE', 'AUTO', 'LOW', 'MEDIUM', 'HIGH'] | None = None
