from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EndUserMessagingProtectConfigurationRuleSetNumberOverride(BaseModel):
    DestinationPhoneNumber: StrictStr | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
    Action: StrictStr | None = None
    IsoCountryCode: StrictStr | None = None
    ExpirationTimestamp: datetime.datetime | StrictStr | None = None
