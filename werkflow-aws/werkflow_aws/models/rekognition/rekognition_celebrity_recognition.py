from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .rekognition_celebrity_detail import RekognitionCelebrityDetail


class RekognitionCelebrityRecognition(BaseModel):
    Timestamp: StrictInt | None = None
    Celebrity: RekognitionCelebrityDetail | None = None
