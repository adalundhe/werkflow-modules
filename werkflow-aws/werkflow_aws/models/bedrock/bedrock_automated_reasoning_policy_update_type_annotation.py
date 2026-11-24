from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_automated_reasoning_policy_type_value_annotation import BedrockAutomatedReasoningPolicyTypeValueAnnotation


class BedrockAutomatedReasoningPolicyUpdateTypeAnnotation(BaseModel):
    name: StrictStr | None = None
    newName: StrictStr | None = None
    description: StrictStr | None = None
    values: list[BedrockAutomatedReasoningPolicyTypeValueAnnotation] | None = None
