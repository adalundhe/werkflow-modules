from __future__ import annotations
from pydantic import BaseModel
from .bedrock_runtime_guardrail_trace_assessment import BedrockRuntimeGuardrailTraceAssessment
from .bedrock_runtime_prompt_router_trace import BedrockRuntimePromptRouterTrace


class BedrockRuntimeConverseTrace(BaseModel):
    guardrail: BedrockRuntimeGuardrailTraceAssessment | None = None
    promptRouter: BedrockRuntimePromptRouterTrace | None = None
