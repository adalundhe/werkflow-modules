from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConfigServiceOrganizationCustomPolicyRuleMetadata(BaseModel):
    PolicyRuntime: StrictStr
    PolicyText: StrictStr
    Description: StrictStr | None = None
    OrganizationConfigRuleTriggerTypes: list[Literal['ConfigurationItemChangeNotification', 'OversizedConfigurationItemChangeNotification']] | None = None
    InputParameters: StrictStr | None = None
    MaximumExecutionFrequency: Literal['One_Hour', 'Three_Hours', 'Six_Hours', 'Twelve_Hours', 'TwentyFour_Hours'] | None = None
    ResourceTypesScope: list[StrictStr] | None = None
    ResourceIdScope: StrictStr | None = None
    TagKeyScope: StrictStr | None = None
    TagValueScope: StrictStr | None = None
    DebugLogDeliveryAccounts: list[StrictStr] | None = None
