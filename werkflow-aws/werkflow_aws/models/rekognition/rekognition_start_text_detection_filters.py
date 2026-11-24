from __future__ import annotations
from pydantic import BaseModel
from .rekognition_detection_filter import RekognitionDetectionFilter
from .rekognition_region_of_interest import RekognitionRegionOfInterest


class RekognitionStartTextDetectionFilters(BaseModel):
    WordFilter: RekognitionDetectionFilter | None = None
    RegionsOfInterest: list[RekognitionRegionOfInterest] | None = None
