from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .config_service_organization_custom_policy_rule_metadata import ConfigServiceOrganizationCustomPolicyRuleMetadata
from .config_service_organization_custom_rule_metadata import ConfigServiceOrganizationCustomRuleMetadata
from .config_service_organization_managed_rule_metadata import ConfigServiceOrganizationManagedRuleMetadata
from .config_service_tag import ConfigServiceTag


class ConfigServicePutOrganizationConfigRuleRequest(BaseModel):
    OrganizationConfigRuleName: StrictStr
    OrganizationManagedRuleMetadata: ConfigServiceOrganizationManagedRuleMetadata | None = None
    OrganizationCustomRuleMetadata: ConfigServiceOrganizationCustomRuleMetadata | None = None
    ExcludedAccounts: list[StrictStr] | None = None
    OrganizationCustomPolicyRuleMetadata: ConfigServiceOrganizationCustomPolicyRuleMetadata | None = None
    Tags: list[ConfigServiceTag] | None = None
