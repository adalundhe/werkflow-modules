from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_invocation_logs_config import BedrockInvocationLogsConfig


class BedrockTrainingDataConfig(BaseModel):
    s3Uri: StrictStr | None = None
    invocationLogsConfig: BedrockInvocationLogsConfig | None = None
