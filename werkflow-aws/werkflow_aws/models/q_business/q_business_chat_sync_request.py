from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .q_business_action_execution import QBusinessActionExecution
from .q_business_attachment_input import QBusinessAttachmentInput
from .q_business_attribute_filter import QBusinessAttributeFilter
from .q_business_auth_challenge_response import QBusinessAuthChallengeResponse
from .q_business_chat_mode_configuration import QBusinessChatModeConfiguration


class QBusinessChatSyncRequest(BaseModel):
    applicationId: StrictStr
    userId: StrictStr | None = None
    userGroups: list[StrictStr] | None = None
    userMessage: StrictStr | None = None
    attachments: list[QBusinessAttachmentInput] | None = None
    actionExecution: QBusinessActionExecution | None = None
    authChallengeResponse: QBusinessAuthChallengeResponse | None = None
    conversationId: StrictStr | None = None
    parentMessageId: StrictStr | None = None
    attributeFilter: QBusinessAttributeFilter | None = None
    chatMode: Literal['RETRIEVAL_MODE', 'CREATOR_MODE', 'PLUGIN_MODE'] | None = None
    chatModeConfiguration: QBusinessChatModeConfiguration | None = None
    clientToken: StrictStr | None = None
