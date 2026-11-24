from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .config_service_organization_custom_policy_rule_metadata_no_policy import ConfigServiceOrganizationCustomPolicyRuleMetadataNoPolicy
from .config_service_organization_custom_rule_metadata import ConfigServiceOrganizationCustomRuleMetadata
from .config_service_organization_managed_rule_metadata import ConfigServiceOrganizationManagedRuleMetadata


class ConfigServiceOrganizationConfigRule(BaseModel):
    OrganizationConfigRuleName: StrictStr | None = None
    OrganizationConfigRuleArn: StrictStr | None = None
    OrganizationManagedRuleMetadata: ConfigServiceOrganizationManagedRuleMetadata | None = None
    OrganizationCustomRuleMetadata: ConfigServiceOrganizationCustomRuleMetadata | None = None
    ExcludedAccounts: list[StrictStr] | None = None
    LastUpdateTime: datetime.datetime | StrictStr | None = None
    OrganizationCustomPolicyRuleMetadata: ConfigServiceOrganizationCustomPolicyRuleMetadataNoPolicy | None = None
