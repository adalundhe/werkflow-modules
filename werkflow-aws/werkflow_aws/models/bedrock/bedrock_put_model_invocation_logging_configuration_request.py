from __future__ import annotations
from pydantic import BaseModel
from .bedrock_logging_config import BedrockLoggingConfig


class BedrockPutModelInvocationLoggingConfigurationRequest(BaseModel):
    loggingConfig: BedrockLoggingConfig
