from __future__ import annotations
from pydantic import BaseModel
from .q_business_audio_source_details import QBusinessAudioSourceDetails
from .q_business_image_source_details import QBusinessImageSourceDetails
from .q_business_video_source_details import QBusinessVideoSourceDetails


class QBusinessSourceDetails(BaseModel):
    imageSourceDetails: QBusinessImageSourceDetails | None = None
    audioSourceDetails: QBusinessAudioSourceDetails | None = None
    videoSourceDetails: QBusinessVideoSourceDetails | None = None
