from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingAssociateProtectConfigurationRequest(BaseModel):
    ProtectConfigurationId: StrictStr
    ConfigurationSetName: StrictStr
