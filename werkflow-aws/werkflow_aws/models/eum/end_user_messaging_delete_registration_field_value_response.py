from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class EndUserMessagingDeleteRegistrationFieldValueResponse(BaseModel):
    RegistrationArn: StrictStr | None = None
    RegistrationId: StrictStr | None = None
    VersionNumber: StrictInt | None = None
    FieldPath: StrictStr | None = None
    SelectChoices: list[StrictStr] | None = None
    TextValue: StrictStr | None = None
    RegistrationAttachmentId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
