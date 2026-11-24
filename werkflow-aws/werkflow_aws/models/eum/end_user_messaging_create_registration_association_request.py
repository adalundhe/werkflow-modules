from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingCreateRegistrationAssociationRequest(BaseModel):
    RegistrationId: StrictStr
    ResourceId: StrictStr
