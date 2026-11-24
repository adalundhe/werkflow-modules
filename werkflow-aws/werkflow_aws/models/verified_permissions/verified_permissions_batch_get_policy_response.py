from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .verified_permissions_batch_get_policy_error_item import VerifiedPermissionsBatchGetPolicyErrorItem
from .verified_permissions_batch_get_policy_output_item import VerifiedPermissionsBatchGetPolicyOutputItem


class VerifiedPermissionsBatchGetPolicyResponse(BaseModel):
    results: list[VerifiedPermissionsBatchGetPolicyOutputItem] | None = None
    errors: list[VerifiedPermissionsBatchGetPolicyErrorItem] | None = None
    ResponseMetadata: dict[str, Any] | None = None
