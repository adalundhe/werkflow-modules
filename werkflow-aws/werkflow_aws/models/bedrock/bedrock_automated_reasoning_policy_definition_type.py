from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_automated_reasoning_policy_definition_type_value import BedrockAutomatedReasoningPolicyDefinitionTypeValue


class BedrockAutomatedReasoningPolicyDefinitionType(BaseModel):
    name: StrictStr | None = None
    description: StrictStr | None = None
    values: list[BedrockAutomatedReasoningPolicyDefinitionTypeValue] | None = None
