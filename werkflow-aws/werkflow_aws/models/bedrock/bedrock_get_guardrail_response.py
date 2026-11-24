from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_guardrail_automated_reasoning_policy import BedrockGuardrailAutomatedReasoningPolicy
from .bedrock_guardrail_content_policy import BedrockGuardrailContentPolicy
from .bedrock_guardrail_contextual_grounding_policy import BedrockGuardrailContextualGroundingPolicy
from .bedrock_guardrail_cross_region_details import BedrockGuardrailCrossRegionDetails
from .bedrock_guardrail_sensitive_information_policy import BedrockGuardrailSensitiveInformationPolicy
from .bedrock_guardrail_topic_policy import BedrockGuardrailTopicPolicy
from .bedrock_guardrail_word_policy import BedrockGuardrailWordPolicy


class BedrockGetGuardrailResponse(BaseModel):
    name: StrictStr | None = None
    description: StrictStr | None = None
    guardrailId: StrictStr | None = None
    guardrailArn: StrictStr | None = None
    version: StrictStr | None = None
    status: StrictStr | None = None
    topicPolicy: BedrockGuardrailTopicPolicy | None = None
    contentPolicy: BedrockGuardrailContentPolicy | None = None
    wordPolicy: BedrockGuardrailWordPolicy | None = None
    sensitiveInformationPolicy: BedrockGuardrailSensitiveInformationPolicy | None = None
    contextualGroundingPolicy: BedrockGuardrailContextualGroundingPolicy | None = None
    automatedReasoningPolicy: BedrockGuardrailAutomatedReasoningPolicy | None = None
    crossRegionDetails: BedrockGuardrailCrossRegionDetails | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    statusReasons: list[StrictStr] | None = None
    failureRecommendations: list[StrictStr] | None = None
    blockedInputMessaging: StrictStr | None = None
    blockedOutputsMessaging: StrictStr | None = None
    kmsKeyArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
