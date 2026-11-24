from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .end_user_messaging_protect_configuration_country_rule_set_information import EndUserMessagingProtectConfigurationCountryRuleSetInformation


class EndUserMessagingUpdateProtectConfigurationCountryRuleSetResponse(BaseModel):
    ProtectConfigurationArn: StrictStr | None = None
    ProtectConfigurationId: StrictStr | None = None
    NumberCapability: StrictStr | None = None
    CountryRuleSet: dict[StrictStr, EndUserMessagingProtectConfigurationCountryRuleSetInformation] | None = None
    ResponseMetadata: dict[str, Any] | None = None
