from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .aws_secrets_manager_resource_policy_summary import AWSSecretsManagerResourcePolicySummary


class AWSSecretsManagerListResourcePoliciesResponse(BaseModel):
    ResourcePolicies: list[AWSSecretsManagerResourcePolicySummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
