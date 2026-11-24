from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceOrganizationCustomRuleMetadata(BaseModel):
    Description: StrictStr | None = None
    LambdaFunctionArn: StrictStr | None = None
    OrganizationConfigRuleTriggerTypes: list[StrictStr] | None = None
    InputParameters: StrictStr | None = None
    MaximumExecutionFrequency: StrictStr | None = None
    ResourceTypesScope: list[StrictStr] | None = None
    ResourceIdScope: StrictStr | None = None
    TagKeyScope: StrictStr | None = None
    TagValueScope: StrictStr | None = None
