from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .end_user_messaging_protect_configuration_country_rule_set_information import EndUserMessagingProtectConfigurationCountryRuleSetInformation


class EndUserMessagingUpdateProtectConfigurationCountryRuleSetRequest(BaseModel):
    ProtectConfigurationId: StrictStr
    NumberCapability: Literal['SMS', 'VOICE', 'MMS', 'RCS']
    CountryRuleSetUpdates: dict[StrictStr, EndUserMessagingProtectConfigurationCountryRuleSetInformation]
