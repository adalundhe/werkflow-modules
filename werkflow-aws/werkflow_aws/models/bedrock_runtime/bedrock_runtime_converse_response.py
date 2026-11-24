from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_runtime_converse_metrics import BedrockRuntimeConverseMetrics
from .bedrock_runtime_converse_output import BedrockRuntimeConverseOutput
from .bedrock_runtime_converse_trace import BedrockRuntimeConverseTrace
from .bedrock_runtime_document import BedrockRuntimeDocument
from .bedrock_runtime_performance_configuration import BedrockRuntimePerformanceConfiguration
from .bedrock_runtime_service_tier import BedrockRuntimeServiceTier
from .bedrock_runtime_token_usage import BedrockRuntimeTokenUsage


class BedrockRuntimeConverseResponse(BaseModel):
    output: BedrockRuntimeConverseOutput | None = None
    stopReason: StrictStr | None = None
    usage: BedrockRuntimeTokenUsage | None = None
    metrics: BedrockRuntimeConverseMetrics | None = None
    additionalModelResponseFields: BedrockRuntimeDocument | None = None
    trace: BedrockRuntimeConverseTrace | None = None
    performanceConfig: BedrockRuntimePerformanceConfiguration | None = None
    serviceTier: BedrockRuntimeServiceTier | None = None
    ResponseMetadata: dict[str, Any] | None = None
