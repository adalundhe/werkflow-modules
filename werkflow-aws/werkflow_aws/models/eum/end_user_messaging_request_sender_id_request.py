from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .end_user_messaging_tag import EndUserMessagingTag


class EndUserMessagingRequestSenderIdRequest(BaseModel):
    SenderId: StrictStr
    IsoCountryCode: StrictStr
    MessageTypes: list[Literal['TRANSACTIONAL', 'PROMOTIONAL']] | None = None
    DeletionProtectionEnabled: StrictBool | None = None
    Tags: list[EndUserMessagingTag] | None = None
    ClientToken: StrictStr | None = None
