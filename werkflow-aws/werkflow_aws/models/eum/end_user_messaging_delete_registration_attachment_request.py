from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingDeleteRegistrationAttachmentRequest(BaseModel):
    RegistrationAttachmentId: StrictStr
