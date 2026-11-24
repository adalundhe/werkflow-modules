from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .end_user_messaging_conditional_validation import EndUserMessagingConditionalValidation
from .end_user_messaging_field_condition import EndUserMessagingFieldCondition


class EndUserMessagingConditionalRule(BaseModel):
    Conditions: list[EndUserMessagingFieldCondition] | None = None
    RuleBehavior: StrictStr | None = None
    ConditionalValidation: EndUserMessagingConditionalValidation | None = None
