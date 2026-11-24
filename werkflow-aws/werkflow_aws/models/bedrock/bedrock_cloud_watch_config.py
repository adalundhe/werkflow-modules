from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_s3_config import BedrockS3Config


class BedrockCloudWatchConfig(BaseModel):
    logGroupName: StrictStr | None = None
    roleArn: StrictStr | None = None
    largeDataDeliveryS3Config: BedrockS3Config | None = None
