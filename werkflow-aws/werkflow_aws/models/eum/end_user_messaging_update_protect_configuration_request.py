from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EndUserMessagingUpdateProtectConfigurationRequest(BaseModel):
    ProtectConfigurationId: StrictStr
    DeletionProtectionEnabled: StrictBool | None = None
