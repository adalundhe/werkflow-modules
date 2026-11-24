from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_association_filters import SecurityHubAssociationFilters


class SecurityHubListConfigurationPolicyAssociationsRequest(BaseModel):
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    Filters: SecurityHubAssociationFilters | None = None
