from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_guardrail_automated_reasoning_policy_config import BedrockGuardrailAutomatedReasoningPolicyConfig
from .bedrock_guardrail_content_policy_config import BedrockGuardrailContentPolicyConfig
from .bedrock_guardrail_contextual_grounding_policy_config import BedrockGuardrailContextualGroundingPolicyConfig
from .bedrock_guardrail_cross_region_config import BedrockGuardrailCrossRegionConfig
from .bedrock_guardrail_sensitive_information_policy_config import BedrockGuardrailSensitiveInformationPolicyConfig
from .bedrock_guardrail_topic_policy_config import BedrockGuardrailTopicPolicyConfig
from .bedrock_guardrail_word_policy_config import BedrockGuardrailWordPolicyConfig


class BedrockUpdateGuardrailRequest(BaseModel):
    guardrailIdentifier: StrictStr
    name: StrictStr
    blockedInputMessaging: StrictStr
    blockedOutputsMessaging: StrictStr
    description: StrictStr | None = None
    topicPolicyConfig: BedrockGuardrailTopicPolicyConfig | None = None
    contentPolicyConfig: BedrockGuardrailContentPolicyConfig | None = None
    wordPolicyConfig: BedrockGuardrailWordPolicyConfig | None = None
    sensitiveInformationPolicyConfig: BedrockGuardrailSensitiveInformationPolicyConfig | None = None
    contextualGroundingPolicyConfig: BedrockGuardrailContextualGroundingPolicyConfig | None = None
    automatedReasoningPolicyConfig: BedrockGuardrailAutomatedReasoningPolicyConfig | None = None
    crossRegionConfig: BedrockGuardrailCrossRegionConfig | None = None
    kmsKeyId: StrictStr | None = None
