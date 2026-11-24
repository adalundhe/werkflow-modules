from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingDeleteProtectConfigurationRuleSetNumberOverrideRequest(BaseModel):
    ProtectConfigurationId: StrictStr
    DestinationPhoneNumber: StrictStr
