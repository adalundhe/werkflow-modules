from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .end_user_messaging_protect_configuration_rule_set_number_override_filter_item import EndUserMessagingProtectConfigurationRuleSetNumberOverrideFilterItem


class EndUserMessagingListProtectConfigurationRuleSetNumberOverridesRequest(BaseModel):
    ProtectConfigurationId: StrictStr
    Filters: list[EndUserMessagingProtectConfigurationRuleSetNumberOverrideFilterItem] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
