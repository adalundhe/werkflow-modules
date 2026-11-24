from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .verified_permissions_policy_item import VerifiedPermissionsPolicyItem


class VerifiedPermissionsListPoliciesResponse(BaseModel):
    nextToken: StrictStr | None = None
    policies: list[VerifiedPermissionsPolicyItem] | None = None
    ResponseMetadata: dict[str, Any] | None = None
