from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_hub_configuration_policy_association_summary import SecurityHubConfigurationPolicyAssociationSummary


class SecurityHubListConfigurationPolicyAssociationsResponse(BaseModel):
    ConfigurationPolicyAssociationSummaries: list[SecurityHubConfigurationPolicyAssociationSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
