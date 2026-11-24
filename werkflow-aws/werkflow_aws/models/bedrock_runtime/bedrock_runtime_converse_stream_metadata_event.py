from __future__ import annotations
from pydantic import BaseModel
from .bedrock_runtime_converse_stream_metrics import BedrockRuntimeConverseStreamMetrics
from .bedrock_runtime_converse_stream_trace import BedrockRuntimeConverseStreamTrace
from .bedrock_runtime_performance_configuration import BedrockRuntimePerformanceConfiguration
from .bedrock_runtime_service_tier import BedrockRuntimeServiceTier
from .bedrock_runtime_token_usage import BedrockRuntimeTokenUsage


class BedrockRuntimeConverseStreamMetadataEvent(BaseModel):
    usage: BedrockRuntimeTokenUsage | None = None
    metrics: BedrockRuntimeConverseStreamMetrics | None = None
    trace: BedrockRuntimeConverseStreamTrace | None = None
    performanceConfig: BedrockRuntimePerformanceConfiguration | None = None
    serviceTier: BedrockRuntimeServiceTier | None = None
