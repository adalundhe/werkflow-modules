from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .q_business_action_review_payload_field import QBusinessActionReviewPayloadField


class QBusinessActionReviewEvent(BaseModel):
    conversationId: StrictStr | None = None
    userMessageId: StrictStr | None = None
    systemMessageId: StrictStr | None = None
    pluginId: StrictStr | None = None
    pluginType: StrictStr | None = None
    payload: dict[StrictStr, QBusinessActionReviewPayloadField] | None = None
    payloadFieldNameSeparator: StrictStr | None = None
