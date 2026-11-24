from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingRegistrationFieldValueInformation(BaseModel):
    FieldPath: StrictStr | None = None
    SelectChoices: list[StrictStr] | None = None
    TextValue: StrictStr | None = None
    RegistrationAttachmentId: StrictStr | None = None
    DeniedReason: StrictStr | None = None
    Feedback: StrictStr | None = None
