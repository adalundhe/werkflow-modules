from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .security_hub_configuration_policy_association_summary import SecurityHubConfigurationPolicyAssociationSummary
from .security_hub_unprocessed_configuration_policy_association import SecurityHubUnprocessedConfigurationPolicyAssociation


class SecurityHubBatchGetConfigurationPolicyAssociationsResponse(BaseModel):
    ConfigurationPolicyAssociations: list[SecurityHubConfigurationPolicyAssociationSummary] | None = None
    UnprocessedConfigurationPolicyAssociations: list[SecurityHubUnprocessedConfigurationPolicyAssociation] | None = None
    ResponseMetadata: dict[str, Any] | None = None
