from __future__ import annotations
from pydantic import BaseModel
from .q_business_audio_extraction_configuration import QBusinessAudioExtractionConfiguration
from .q_business_image_extraction_configuration import QBusinessImageExtractionConfiguration
from .q_business_video_extraction_configuration import QBusinessVideoExtractionConfiguration


class QBusinessMediaExtractionConfiguration(BaseModel):
    imageExtractionConfiguration: QBusinessImageExtractionConfiguration | None = None
    audioExtractionConfiguration: QBusinessAudioExtractionConfiguration | None = None
    videoExtractionConfiguration: QBusinessVideoExtractionConfiguration | None = None
