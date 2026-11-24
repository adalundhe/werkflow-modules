from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .kinesis_video_image_generation_configuration import KinesisVideoImageGenerationConfiguration


class KinesisVideoDescribeImageGenerationConfigurationResponse(BaseModel):
    ImageGenerationConfiguration: KinesisVideoImageGenerationConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
