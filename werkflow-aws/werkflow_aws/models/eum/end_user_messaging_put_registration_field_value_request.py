from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingPutRegistrationFieldValueRequest(BaseModel):
    RegistrationId: StrictStr
    FieldPath: StrictStr
    SelectChoices: list[StrictStr] | None = None
    TextValue: StrictStr | None = None
    RegistrationAttachmentId: StrictStr | None = None
