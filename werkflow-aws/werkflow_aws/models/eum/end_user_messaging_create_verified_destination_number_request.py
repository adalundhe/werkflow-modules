from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .end_user_messaging_tag import EndUserMessagingTag


class EndUserMessagingCreateVerifiedDestinationNumberRequest(BaseModel):
    DestinationPhoneNumber: StrictStr
    RcsAgentId: StrictStr | None = None
    Tags: list[EndUserMessagingTag] | None = None
    ClientToken: StrictStr | None = None
