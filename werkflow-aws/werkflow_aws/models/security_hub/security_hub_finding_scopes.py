from __future__ import annotations
from pydantic import BaseModel
from .security_hub_aws_organization_scope import SecurityHubAwsOrganizationScope


class SecurityHubFindingScopes(BaseModel):
    AwsOrganizations: list[SecurityHubAwsOrganizationScope] | None = None
