from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class EndUserMessagingUpdateNotifyConfigurationRequest(BaseModel):
    NotifyConfigurationId: StrictStr
    DefaultTemplateId: StrictStr | None = None
    PoolId: StrictStr | None = None
    EnabledCountries: list[StrictStr] | None = None
    EnabledChannels: list[Literal['SMS', 'VOICE', 'MMS', 'RCS']] | None = None
    DeletionProtectionEnabled: StrictBool | None = None
