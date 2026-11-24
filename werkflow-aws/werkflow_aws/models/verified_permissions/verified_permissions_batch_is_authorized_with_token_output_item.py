from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .verified_permissions_batch_is_authorized_with_token_input_item import VerifiedPermissionsBatchIsAuthorizedWithTokenInputItem
from .verified_permissions_determining_policy_item import VerifiedPermissionsDeterminingPolicyItem
from .verified_permissions_evaluation_error_item import VerifiedPermissionsEvaluationErrorItem


class VerifiedPermissionsBatchIsAuthorizedWithTokenOutputItem(BaseModel):
    request: VerifiedPermissionsBatchIsAuthorizedWithTokenInputItem | None = None
    decision: StrictStr | None = None
    determiningPolicies: list[VerifiedPermissionsDeterminingPolicyItem] | None = None
    errors: list[VerifiedPermissionsEvaluationErrorItem] | None = None
