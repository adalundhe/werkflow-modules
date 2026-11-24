from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .q_business_action_review_payload_field import QBusinessActionReviewPayloadField


class QBusinessActionReview(BaseModel):
    pluginId: StrictStr | None = None
    pluginType: StrictStr | None = None
    payload: dict[StrictStr, QBusinessActionReviewPayloadField] | None = None
    payloadFieldNameSeparator: StrictStr | None = None
