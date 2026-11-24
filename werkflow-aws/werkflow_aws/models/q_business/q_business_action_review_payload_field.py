from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .q_business_action_payload_field_value import QBusinessActionPayloadFieldValue
from .q_business_action_review_payload_field_allowed_value import QBusinessActionReviewPayloadFieldAllowedValue
from .q_business_action_review_payload_field_array_item_json_schema import QBusinessActionReviewPayloadFieldArrayItemJsonSchema


class QBusinessActionReviewPayloadField(BaseModel):
    displayName: StrictStr | None = None
    displayOrder: StrictInt | None = None
    displayDescription: StrictStr | None = None
    type: StrictStr | None = None
    value: QBusinessActionPayloadFieldValue | None = None
    allowedValues: list[QBusinessActionReviewPayloadFieldAllowedValue] | None = None
    allowedFormat: StrictStr | None = None
    arrayItemJsonSchema: QBusinessActionReviewPayloadFieldArrayItemJsonSchema | None = None
    required: StrictBool | None = None
