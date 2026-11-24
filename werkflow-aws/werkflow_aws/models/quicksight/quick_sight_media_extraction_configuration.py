from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_audio_extraction_configuration import QuickSightAudioExtractionConfiguration
from .quick_sight_image_extraction_configuration import QuickSightImageExtractionConfiguration
from .quick_sight_video_extraction_configuration import QuickSightVideoExtractionConfiguration


class QuickSightMediaExtractionConfiguration(BaseModel):
    imageExtractionConfiguration: QuickSightImageExtractionConfiguration | None = None
    audioExtractionConfiguration: QuickSightAudioExtractionConfiguration | None = None
    videoExtractionConfiguration: QuickSightVideoExtractionConfiguration | None = None
