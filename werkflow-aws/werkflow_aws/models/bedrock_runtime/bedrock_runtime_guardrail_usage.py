from __future__ import annotations
from pydantic import BaseModel, StrictInt


class BedrockRuntimeGuardrailUsage(BaseModel):
    topicPolicyUnits: StrictInt | None = None
    contentPolicyUnits: StrictInt | None = None
    wordPolicyUnits: StrictInt | None = None
    sensitiveInformationPolicyUnits: StrictInt | None = None
    sensitiveInformationPolicyFreeUnits: StrictInt | None = None
    contextualGroundingPolicyUnits: StrictInt | None = None
    contentPolicyImageUnits: StrictInt | None = None
    automatedReasoningPolicyUnits: StrictInt | None = None
    automatedReasoningPolicies: StrictInt | None = None
