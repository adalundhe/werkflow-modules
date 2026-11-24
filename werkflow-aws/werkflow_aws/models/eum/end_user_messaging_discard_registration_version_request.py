from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingDiscardRegistrationVersionRequest(BaseModel):
    RegistrationId: StrictStr
