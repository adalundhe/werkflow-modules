from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr


class EndUserMessagingPutProtectConfigurationRuleSetNumberOverrideRequest(BaseModel):
    ProtectConfigurationId: StrictStr
    DestinationPhoneNumber: StrictStr
    Action: Literal['ALLOW', 'BLOCK']
    ClientToken: StrictStr | None = None
    ExpirationTimestamp: datetime.datetime | StrictStr | None = None
