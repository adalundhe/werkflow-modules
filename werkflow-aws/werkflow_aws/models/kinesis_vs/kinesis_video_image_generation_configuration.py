from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .kinesis_video_image_generation_destination_config import KinesisVideoImageGenerationDestinationConfig


class KinesisVideoImageGenerationConfiguration(BaseModel):
    Status: StrictStr | None = None
    ImageSelectorType: StrictStr | None = None
    DestinationConfig: KinesisVideoImageGenerationDestinationConfig | None = None
    SamplingInterval: StrictInt | None = None
    Format: StrictStr | None = None
    FormatConfig: dict[StrictStr, StrictStr] | None = None
    WidthPixels: StrictInt | None = None
    HeightPixels: StrictInt | None = None
