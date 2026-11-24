from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_iam_attached_managed_policy import SecurityHubAwsIamAttachedManagedPolicy
from .security_hub_aws_iam_permissions_boundary import SecurityHubAwsIamPermissionsBoundary
from .security_hub_aws_iam_user_policy import SecurityHubAwsIamUserPolicy


class SecurityHubAwsIamUserDetails(BaseModel):
    AttachedManagedPolicies: list[SecurityHubAwsIamAttachedManagedPolicy] | None = None
    CreateDate: StrictStr | None = None
    GroupList: list[StrictStr] | None = None
    Path: StrictStr | None = None
    PermissionsBoundary: SecurityHubAwsIamPermissionsBoundary | None = None
    UserId: StrictStr | None = None
    UserName: StrictStr | None = None
    UserPolicyList: list[SecurityHubAwsIamUserPolicy] | None = None
