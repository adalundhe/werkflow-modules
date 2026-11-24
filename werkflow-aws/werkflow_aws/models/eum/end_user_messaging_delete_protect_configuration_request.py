from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingDeleteProtectConfigurationRequest(BaseModel):
    ProtectConfigurationId: StrictStr
