from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingDisassociateProtectConfigurationRequest(BaseModel):
    ProtectConfigurationId: StrictStr
    ConfigurationSetName: StrictStr
