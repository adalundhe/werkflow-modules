from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_video_image_generation_configuration import KinesisVideoImageGenerationConfiguration


class KinesisVideoUpdateImageGenerationConfigurationRequest(BaseModel):
    StreamName: StrictStr | None = None
    StreamARN: StrictStr | None = None
    ImageGenerationConfiguration: KinesisVideoImageGenerationConfiguration | None = None
