from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .bedrock_invocation_log_source import BedrockInvocationLogSource
from .bedrock_request_metadata_filters import BedrockRequestMetadataFilters


class BedrockInvocationLogsConfig(BaseModel):
    usePromptResponse: StrictBool | None = None
    invocationLogSource: BedrockInvocationLogSource | None = None
    requestMetadataFilters: BedrockRequestMetadataFilters | None = None
