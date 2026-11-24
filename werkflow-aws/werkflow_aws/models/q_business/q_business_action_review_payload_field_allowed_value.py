from __future__ import annotations
from pydantic import BaseModel
from .q_business_action_payload_field_value import QBusinessActionPayloadFieldValue


class QBusinessActionReviewPayloadFieldAllowedValue(BaseModel):
    value: QBusinessActionPayloadFieldValue | None = None
    displayValue: QBusinessActionPayloadFieldValue | None = None
