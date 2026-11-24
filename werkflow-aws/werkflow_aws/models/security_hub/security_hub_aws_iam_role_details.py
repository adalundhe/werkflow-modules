from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_aws_iam_attached_managed_policy import SecurityHubAwsIamAttachedManagedPolicy
from .security_hub_aws_iam_instance_profile import SecurityHubAwsIamInstanceProfile
from .security_hub_aws_iam_permissions_boundary import SecurityHubAwsIamPermissionsBoundary
from .security_hub_aws_iam_role_policy import SecurityHubAwsIamRolePolicy


class SecurityHubAwsIamRoleDetails(BaseModel):
    AssumeRolePolicyDocument: StrictStr | None = None
    AttachedManagedPolicies: list[SecurityHubAwsIamAttachedManagedPolicy] | None = None
    CreateDate: StrictStr | None = None
    InstanceProfileList: list[SecurityHubAwsIamInstanceProfile] | None = None
    PermissionsBoundary: SecurityHubAwsIamPermissionsBoundary | None = None
    RoleId: StrictStr | None = None
    RoleName: StrictStr | None = None
    RolePolicyList: list[SecurityHubAwsIamRolePolicy] | None = None
    MaxSessionDuration: StrictInt | None = None
    Path: StrictStr | None = None
