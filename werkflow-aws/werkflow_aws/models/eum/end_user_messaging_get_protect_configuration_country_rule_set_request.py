from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EndUserMessagingGetProtectConfigurationCountryRuleSetRequest(BaseModel):
    ProtectConfigurationId: StrictStr
    NumberCapability: Literal['SMS', 'VOICE', 'MMS', 'RCS']
