from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .q_business_applied_creator_mode_configuration import QBusinessAppliedCreatorModeConfiguration
from .q_business_applied_orchestration_configuration import QBusinessAppliedOrchestrationConfiguration
from .q_business_blocked_phrases_configuration import QBusinessBlockedPhrasesConfiguration
from .q_business_hallucination_reduction_configuration import QBusinessHallucinationReductionConfiguration
from .q_business_topic_configuration import QBusinessTopicConfiguration


class QBusinessGetChatControlsConfigurationResponse(BaseModel):
    responseScope: StrictStr | None = None
    orchestrationConfiguration: QBusinessAppliedOrchestrationConfiguration | None = None
    blockedPhrases: QBusinessBlockedPhrasesConfiguration | None = None
    topicConfigurations: list[QBusinessTopicConfiguration] | None = None
    creatorModeConfiguration: QBusinessAppliedCreatorModeConfiguration | None = None
    nextToken: StrictStr | None = None
    hallucinationReductionConfiguration: QBusinessHallucinationReductionConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
