from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .rekognition_black_frame import RekognitionBlackFrame


class RekognitionStartTechnicalCueDetectionFilter(BaseModel):
    MinSegmentConfidence: StrictFloat | StrictInt | None = None
    BlackFrame: RekognitionBlackFrame | None = None
