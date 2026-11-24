from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .q_business_action_review import QBusinessActionReview
from .q_business_attachment_output import QBusinessAttachmentOutput
from .q_business_auth_challenge_request import QBusinessAuthChallengeRequest
from .q_business_source_attribution import QBusinessSourceAttribution


class QBusinessChatSyncResponse(BaseModel):
    conversationId: StrictStr | None = None
    systemMessage: StrictStr | None = None
    systemMessageId: StrictStr | None = None
    userMessageId: StrictStr | None = None
    actionReview: QBusinessActionReview | None = None
    authChallengeRequest: QBusinessAuthChallengeRequest | None = None
    sourceAttributions: list[QBusinessSourceAttribution] | None = None
    failedAttachments: list[QBusinessAttachmentOutput] | None = None
    ResponseMetadata: dict[str, Any] | None = None
