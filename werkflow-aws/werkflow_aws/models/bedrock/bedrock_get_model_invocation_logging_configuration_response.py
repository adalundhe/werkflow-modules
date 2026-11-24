from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .bedrock_logging_config import BedrockLoggingConfig


class BedrockGetModelInvocationLoggingConfigurationResponse(BaseModel):
    loggingConfig: BedrockLoggingConfig | None = None
    ResponseMetadata: dict[str, Any] | None = None
