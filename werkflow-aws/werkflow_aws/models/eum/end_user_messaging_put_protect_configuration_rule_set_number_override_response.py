from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class EndUserMessagingPutProtectConfigurationRuleSetNumberOverrideResponse(BaseModel):
    ProtectConfigurationArn: StrictStr | None = None
    ProtectConfigurationId: StrictStr | None = None
    DestinationPhoneNumber: StrictStr | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
    Action: StrictStr | None = None
    IsoCountryCode: StrictStr | None = None
    ExpirationTimestamp: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
