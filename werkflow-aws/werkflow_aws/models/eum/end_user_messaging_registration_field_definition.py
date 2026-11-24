from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .end_user_messaging_conditional_behavior import EndUserMessagingConditionalBehavior
from .end_user_messaging_registration_field_display_hints import EndUserMessagingRegistrationFieldDisplayHints
from .end_user_messaging_select_validation import EndUserMessagingSelectValidation
from .end_user_messaging_text_validation import EndUserMessagingTextValidation


class EndUserMessagingRegistrationFieldDefinition(BaseModel):
    SectionPath: StrictStr | None = None
    FieldPath: StrictStr | None = None
    FieldType: StrictStr | None = None
    FieldRequirement: StrictStr | None = None
    SelectValidation: EndUserMessagingSelectValidation | None = None
    TextValidation: EndUserMessagingTextValidation | None = None
    DisplayHints: EndUserMessagingRegistrationFieldDisplayHints | None = None
    ConditionalBehavior: EndUserMessagingConditionalBehavior | None = None
