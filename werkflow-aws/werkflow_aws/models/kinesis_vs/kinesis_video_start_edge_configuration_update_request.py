from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_video_edge_config import KinesisVideoEdgeConfig


class KinesisVideoStartEdgeConfigurationUpdateRequest(BaseModel):
    EdgeConfig: KinesisVideoEdgeConfig
    StreamName: StrictStr | None = None
    StreamARN: StrictStr | None = None
