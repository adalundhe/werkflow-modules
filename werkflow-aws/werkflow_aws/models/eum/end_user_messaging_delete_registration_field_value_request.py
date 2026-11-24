from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingDeleteRegistrationFieldValueRequest(BaseModel):
    RegistrationId: StrictStr
    FieldPath: StrictStr
