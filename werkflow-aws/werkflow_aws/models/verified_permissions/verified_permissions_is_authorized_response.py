from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .verified_permissions_determining_policy_item import VerifiedPermissionsDeterminingPolicyItem
from .verified_permissions_evaluation_error_item import VerifiedPermissionsEvaluationErrorItem


class VerifiedPermissionsIsAuthorizedResponse(BaseModel):
    decision: StrictStr | None = None
    determiningPolicies: list[VerifiedPermissionsDeterminingPolicyItem] | None = None
    errors: list[VerifiedPermissionsEvaluationErrorItem] | None = None
    ResponseMetadata: dict[str, Any] | None = None
