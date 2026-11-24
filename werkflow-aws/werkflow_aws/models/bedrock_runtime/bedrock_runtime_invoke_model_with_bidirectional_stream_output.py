from __future__ import annotations
from pydantic import BaseModel
from .bedrock_runtime_bidirectional_output_payload_part import BedrockRuntimeBidirectionalOutputPayloadPart
from .bedrock_runtime_internal_server_exception import BedrockRuntimeInternalServerException
from .bedrock_runtime_model_stream_error_exception import BedrockRuntimeModelStreamErrorException
from .bedrock_runtime_model_timeout_exception import BedrockRuntimeModelTimeoutException
from .bedrock_runtime_service_unavailable_exception import BedrockRuntimeServiceUnavailableException
from .bedrock_runtime_throttling_exception import BedrockRuntimeThrottlingException
from .bedrock_runtime_validation_exception import BedrockRuntimeValidationException


class BedrockRuntimeInvokeModelWithBidirectionalStreamOutput(BaseModel):
    chunk: BedrockRuntimeBidirectionalOutputPayloadPart | None = None
    internalServerException: BedrockRuntimeInternalServerException | None = None
    modelStreamErrorException: BedrockRuntimeModelStreamErrorException | None = None
    validationException: BedrockRuntimeValidationException | None = None
    throttlingException: BedrockRuntimeThrottlingException | None = None
    modelTimeoutException: BedrockRuntimeModelTimeoutException | None = None
    serviceUnavailableException: BedrockRuntimeServiceUnavailableException | None = None
