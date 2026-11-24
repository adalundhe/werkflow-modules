from __future__ import annotations
from pydantic import BaseModel
from .bedrock_runtime_content_block_delta_event import BedrockRuntimeContentBlockDeltaEvent
from .bedrock_runtime_content_block_start_event import BedrockRuntimeContentBlockStartEvent
from .bedrock_runtime_content_block_stop_event import BedrockRuntimeContentBlockStopEvent
from .bedrock_runtime_converse_stream_metadata_event import BedrockRuntimeConverseStreamMetadataEvent
from .bedrock_runtime_internal_server_exception import BedrockRuntimeInternalServerException
from .bedrock_runtime_message_start_event import BedrockRuntimeMessageStartEvent
from .bedrock_runtime_message_stop_event import BedrockRuntimeMessageStopEvent
from .bedrock_runtime_model_stream_error_exception import BedrockRuntimeModelStreamErrorException
from .bedrock_runtime_service_unavailable_exception import BedrockRuntimeServiceUnavailableException
from .bedrock_runtime_throttling_exception import BedrockRuntimeThrottlingException
from .bedrock_runtime_validation_exception import BedrockRuntimeValidationException


class BedrockRuntimeConverseStreamOutput(BaseModel):
    messageStart: BedrockRuntimeMessageStartEvent | None = None
    contentBlockStart: BedrockRuntimeContentBlockStartEvent | None = None
    contentBlockDelta: BedrockRuntimeContentBlockDeltaEvent | None = None
    contentBlockStop: BedrockRuntimeContentBlockStopEvent | None = None
    messageStop: BedrockRuntimeMessageStopEvent | None = None
    metadata: BedrockRuntimeConverseStreamMetadataEvent | None = None
    internalServerException: BedrockRuntimeInternalServerException | None = None
    modelStreamErrorException: BedrockRuntimeModelStreamErrorException | None = None
    validationException: BedrockRuntimeValidationException | None = None
    throttlingException: BedrockRuntimeThrottlingException | None = None
    serviceUnavailableException: BedrockRuntimeServiceUnavailableException | None = None
