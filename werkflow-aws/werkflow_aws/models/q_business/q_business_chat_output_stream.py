from __future__ import annotations
from pydantic import BaseModel
from .q_business_action_review_event import QBusinessActionReviewEvent
from .q_business_auth_challenge_request_event import QBusinessAuthChallengeRequestEvent
from .q_business_failed_attachment_event import QBusinessFailedAttachmentEvent
from .q_business_metadata_event import QBusinessMetadataEvent
from .q_business_text_output_event import QBusinessTextOutputEvent


class QBusinessChatOutputStream(BaseModel):
    textEvent: QBusinessTextOutputEvent | None = None
    metadataEvent: QBusinessMetadataEvent | None = None
    actionReviewEvent: QBusinessActionReviewEvent | None = None
    failedAttachmentEvent: QBusinessFailedAttachmentEvent | None = None
    authChallengeRequestEvent: QBusinessAuthChallengeRequestEvent | None = None
