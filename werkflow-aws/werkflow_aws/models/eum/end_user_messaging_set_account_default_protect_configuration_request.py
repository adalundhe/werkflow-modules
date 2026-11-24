from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingSetAccountDefaultProtectConfigurationRequest(BaseModel):
    ProtectConfigurationId: StrictStr
