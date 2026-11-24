from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .rekognition_label import RekognitionLabel


class RekognitionLabelDetection(BaseModel):
    Timestamp: StrictInt | None = None
    Label: RekognitionLabel | None = None
    StartTimestampMillis: StrictInt | None = None
    EndTimestampMillis: StrictInt | None = None
    DurationMillis: StrictInt | None = None
