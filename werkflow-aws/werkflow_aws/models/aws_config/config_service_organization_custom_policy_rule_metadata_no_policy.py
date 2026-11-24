from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceOrganizationCustomPolicyRuleMetadataNoPolicy(BaseModel):
    Description: StrictStr | None = None
    OrganizationConfigRuleTriggerTypes: list[StrictStr] | None = None
    InputParameters: StrictStr | None = None
    MaximumExecutionFrequency: StrictStr | None = None
    ResourceTypesScope: list[StrictStr] | None = None
    ResourceIdScope: StrictStr | None = None
    TagKeyScope: StrictStr | None = None
    TagValueScope: StrictStr | None = None
    PolicyRuntime: StrictStr | None = None
    DebugLogDeliveryAccounts: list[StrictStr] | None = None
