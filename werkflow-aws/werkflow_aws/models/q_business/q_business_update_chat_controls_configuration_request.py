from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .q_business_blocked_phrases_configuration_update import QBusinessBlockedPhrasesConfigurationUpdate
from .q_business_creator_mode_configuration import QBusinessCreatorModeConfiguration
from .q_business_hallucination_reduction_configuration import QBusinessHallucinationReductionConfiguration
from .q_business_orchestration_configuration import QBusinessOrchestrationConfiguration
from .q_business_topic_configuration import QBusinessTopicConfiguration


class QBusinessUpdateChatControlsConfigurationRequest(BaseModel):
    applicationId: StrictStr
    clientToken: StrictStr | None = None
    responseScope: Literal['ENTERPRISE_CONTENT_ONLY', 'EXTENDED_KNOWLEDGE_ENABLED'] | None = None
    orchestrationConfiguration: QBusinessOrchestrationConfiguration | None = None
    blockedPhrasesConfigurationUpdate: QBusinessBlockedPhrasesConfigurationUpdate | None = None
    topicConfigurationsToCreateOrUpdate: list[QBusinessTopicConfiguration] | None = None
    topicConfigurationsToDelete: list[QBusinessTopicConfiguration] | None = None
    creatorModeConfiguration: QBusinessCreatorModeConfiguration | None = None
    hallucinationReductionConfiguration: QBusinessHallucinationReductionConfiguration | None = None
