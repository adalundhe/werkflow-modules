from __future__ import annotations
from pydantic import BaseModel
from .rekognition_image import RekognitionImage


class RekognitionRecognizeCelebritiesRequest(BaseModel):
    Image: RekognitionImage
