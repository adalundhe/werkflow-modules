from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .bedrock_cloud_watch_config import BedrockCloudWatchConfig
from .bedrock_s3_config import BedrockS3Config


class BedrockLoggingConfig(BaseModel):
    cloudWatchConfig: BedrockCloudWatchConfig | None = None
    s3Config: BedrockS3Config | None = None
    textDataDeliveryEnabled: StrictBool | None = None
    imageDataDeliveryEnabled: StrictBool | None = None
    embeddingDataDeliveryEnabled: StrictBool | None = None
    videoDataDeliveryEnabled: StrictBool | None = None
    audioDataDeliveryEnabled: StrictBool | None = None
