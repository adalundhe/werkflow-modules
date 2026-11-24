from __future__ import annotations
from pydantic import BaseModel
from .rekognition_start_shot_detection_filter import RekognitionStartShotDetectionFilter
from .rekognition_start_technical_cue_detection_filter import RekognitionStartTechnicalCueDetectionFilter


class RekognitionStartSegmentDetectionFilters(BaseModel):
    TechnicalCueFilter: RekognitionStartTechnicalCueDetectionFilter | None = None
    ShotFilter: RekognitionStartShotDetectionFilter | None = None
