from __future__ import annotations
from pydantic import BaseModel
from .q_business_action_execution_event import QBusinessActionExecutionEvent
from .q_business_attachment_input_event import QBusinessAttachmentInputEvent
from .q_business_auth_challenge_response_event import QBusinessAuthChallengeResponseEvent
from .q_business_configuration_event import QBusinessConfigurationEvent
from .q_business_end_of_input_event import QBusinessEndOfInputEvent
from .q_business_text_input_event import QBusinessTextInputEvent


class QBusinessChatInputStream(BaseModel):
    configurationEvent: QBusinessConfigurationEvent | None = None
    textEvent: QBusinessTextInputEvent | None = None
    attachmentEvent: QBusinessAttachmentInputEvent | None = None
    actionExecutionEvent: QBusinessActionExecutionEvent | None = None
    endOfInputEvent: QBusinessEndOfInputEvent | None = None
    authChallengeResponseEvent: QBusinessAuthChallengeResponseEvent | None = None
