from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rekognition_stream_processing_start_selector import RekognitionStreamProcessingStartSelector
from .rekognition_stream_processing_stop_selector import RekognitionStreamProcessingStopSelector


class RekognitionStartStreamProcessorRequest(BaseModel):
    Name: StrictStr
    StartSelector: RekognitionStreamProcessingStartSelector | None = None
    StopSelector: RekognitionStreamProcessingStopSelector | None = None
