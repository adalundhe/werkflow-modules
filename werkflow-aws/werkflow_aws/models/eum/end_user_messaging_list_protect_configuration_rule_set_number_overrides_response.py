from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .end_user_messaging_protect_configuration_rule_set_number_override import EndUserMessagingProtectConfigurationRuleSetNumberOverride


class EndUserMessagingListProtectConfigurationRuleSetNumberOverridesResponse(BaseModel):
    ProtectConfigurationArn: StrictStr | None = None
    ProtectConfigurationId: StrictStr | None = None
    RuleSetNumberOverrides: list[EndUserMessagingProtectConfigurationRuleSetNumberOverride] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
