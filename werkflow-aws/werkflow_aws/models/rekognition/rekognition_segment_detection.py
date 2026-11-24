from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .rekognition_shot_segment import RekognitionShotSegment
from .rekognition_technical_cue_segment import RekognitionTechnicalCueSegment


class RekognitionSegmentDetection(BaseModel):
    Type: StrictStr | None = None
    StartTimestampMillis: StrictInt | None = None
    EndTimestampMillis: StrictInt | None = None
    DurationMillis: StrictInt | None = None
    StartTimecodeSMPTE: StrictStr | None = None
    EndTimecodeSMPTE: StrictStr | None = None
    DurationSMPTE: StrictStr | None = None
    TechnicalCueSegment: RekognitionTechnicalCueSegment | None = None
    ShotSegment: RekognitionShotSegment | None = None
    StartFrameNumber: StrictInt | None = None
    EndFrameNumber: StrictInt | None = None
    DurationFrames: StrictInt | None = None
