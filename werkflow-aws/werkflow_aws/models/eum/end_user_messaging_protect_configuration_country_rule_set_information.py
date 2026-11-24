from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingProtectConfigurationCountryRuleSetInformation(BaseModel):
    ProtectStatus: StrictStr | None = None
