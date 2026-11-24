from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingDeleteRegistrationRequest(BaseModel):
    RegistrationId: StrictStr
