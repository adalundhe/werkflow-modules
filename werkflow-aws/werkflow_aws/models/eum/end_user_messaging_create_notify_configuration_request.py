from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .end_user_messaging_tag import EndUserMessagingTag


class EndUserMessagingCreateNotifyConfigurationRequest(BaseModel):
    DisplayName: StrictStr
    UseCase: Literal['CODE_VERIFICATION']
    EnabledChannels: list[Literal['SMS', 'VOICE', 'MMS', 'RCS']]
    DefaultTemplateId: StrictStr | None = None
    PoolId: StrictStr | None = None
    EnabledCountries: list[StrictStr] | None = None
    DeletionProtectionEnabled: StrictBool | None = None
    ClientToken: StrictStr | None = None
    Tags: list[EndUserMessagingTag] | None = None
