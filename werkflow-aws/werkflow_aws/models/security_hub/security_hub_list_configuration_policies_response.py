from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_hub_configuration_policy_summary import SecurityHubConfigurationPolicySummary


class SecurityHubListConfigurationPoliciesResponse(BaseModel):
    ConfigurationPolicySummaries: list[SecurityHubConfigurationPolicySummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
