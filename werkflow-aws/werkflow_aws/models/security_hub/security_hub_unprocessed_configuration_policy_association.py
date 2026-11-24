from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_configuration_policy_association import SecurityHubConfigurationPolicyAssociation


class SecurityHubUnprocessedConfigurationPolicyAssociation(BaseModel):
    ConfigurationPolicyAssociationIdentifiers: SecurityHubConfigurationPolicyAssociation | None = None
    ErrorCode: StrictStr | None = None
    ErrorReason: StrictStr | None = None
