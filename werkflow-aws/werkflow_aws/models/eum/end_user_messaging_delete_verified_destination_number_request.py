from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingDeleteVerifiedDestinationNumberRequest(BaseModel):
    VerifiedDestinationNumberId: StrictStr
