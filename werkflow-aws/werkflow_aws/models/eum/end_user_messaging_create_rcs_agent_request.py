from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .end_user_messaging_tag import EndUserMessagingTag


class EndUserMessagingCreateRcsAgentRequest(BaseModel):
    DeletionProtectionEnabled: StrictBool | None = None
    OptOutListName: StrictStr | None = None
    Tags: list[EndUserMessagingTag] | None = None
    ClientToken: StrictStr | None = None
