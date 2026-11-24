from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt
from .open_search_serverless_access_policy_stats import OpenSearchServerlessAccessPolicyStats
from .open_search_serverless_lifecycle_policy_stats import OpenSearchServerlessLifecyclePolicyStats
from .open_search_serverless_security_config_stats import OpenSearchServerlessSecurityConfigStats
from .open_search_serverless_security_policy_stats import OpenSearchServerlessSecurityPolicyStats


class OpenSearchServerlessGetPoliciesStatsResponse(BaseModel):
    AccessPolicyStats: OpenSearchServerlessAccessPolicyStats | None = None
    SecurityPolicyStats: OpenSearchServerlessSecurityPolicyStats | None = None
    SecurityConfigStats: OpenSearchServerlessSecurityConfigStats | None = None
    LifecyclePolicyStats: OpenSearchServerlessLifecyclePolicyStats | None = None
    TotalPolicyCount: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
