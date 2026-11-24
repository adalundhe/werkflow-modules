from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .end_user_messaging_tag import EndUserMessagingTag


class EndUserMessagingCreateProtectConfigurationRequest(BaseModel):
    ClientToken: StrictStr | None = None
    DeletionProtectionEnabled: StrictBool | None = None
    Tags: list[EndUserMessagingTag] | None = None
