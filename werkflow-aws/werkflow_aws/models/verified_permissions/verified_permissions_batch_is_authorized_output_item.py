from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .verified_permissions_batch_is_authorized_input_item import VerifiedPermissionsBatchIsAuthorizedInputItem
from .verified_permissions_determining_policy_item import VerifiedPermissionsDeterminingPolicyItem
from .verified_permissions_evaluation_error_item import VerifiedPermissionsEvaluationErrorItem


class VerifiedPermissionsBatchIsAuthorizedOutputItem(BaseModel):
    request: VerifiedPermissionsBatchIsAuthorizedInputItem | None = None
    decision: StrictStr | None = None
    determiningPolicies: list[VerifiedPermissionsDeterminingPolicyItem] | None = None
    errors: list[VerifiedPermissionsEvaluationErrorItem] | None = None
