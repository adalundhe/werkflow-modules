from __future__ import annotations
from pydantic import BaseModel
from .wa_fv2_bedrock_guardrails_request_and_response import WAFv2BedrockGuardrailsRequestAndResponse
from .wa_fv2_bedrock_guardrails_request_only import WAFv2BedrockGuardrailsRequestOnly
from .wa_fv2_disable_bedrock_guardrails import WAFv2DisableBedrockGuardrails


class WAFv2BedrockGuardrails(BaseModel):
    Disable: WAFv2DisableBedrockGuardrails | None = None
    ProtectRequestOnly: WAFv2BedrockGuardrailsRequestOnly | None = None
    ProtectRequestAndResponse: WAFv2BedrockGuardrailsRequestAndResponse | None = None
