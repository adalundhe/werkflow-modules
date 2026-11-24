from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_bedrock_guardrail_configuration import LexBedrockGuardrailConfiguration


class LexBedrockModelSpecification(BaseModel):
    modelArn: StrictStr | None = None
    guardrail: LexBedrockGuardrailConfiguration | None = None
    traceStatus: StrictStr | None = None
    customPrompt: StrictStr | None = None
