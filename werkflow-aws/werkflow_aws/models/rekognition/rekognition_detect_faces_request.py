from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .rekognition_image import RekognitionImage


class RekognitionDetectFacesRequest(BaseModel):
    Image: RekognitionImage
    Attributes: list[Literal['DEFAULT', 'ALL', 'AGE_RANGE', 'BEARD', 'EMOTIONS', 'EYE_DIRECTION', 'EYEGLASSES', 'EYES_OPEN', 'GENDER', 'MOUTH_OPEN', 'MUSTACHE', 'FACE_OCCLUDED', 'SMILE', 'SUNGLASSES']] | None = None
