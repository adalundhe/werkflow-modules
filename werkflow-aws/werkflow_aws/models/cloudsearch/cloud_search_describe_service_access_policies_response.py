from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_search_access_policies_status import CloudSearchAccessPoliciesStatus


class CloudSearchDescribeServiceAccessPoliciesResponse(BaseModel):
    AccessPolicies: CloudSearchAccessPoliciesStatus | None = None
    ResponseMetadata: dict[str, Any] | None = None
