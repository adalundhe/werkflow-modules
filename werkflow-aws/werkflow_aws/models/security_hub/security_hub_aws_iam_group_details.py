from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_iam_attached_managed_policy import SecurityHubAwsIamAttachedManagedPolicy
from .security_hub_aws_iam_group_policy import SecurityHubAwsIamGroupPolicy


class SecurityHubAwsIamGroupDetails(BaseModel):
    AttachedManagedPolicies: list[SecurityHubAwsIamAttachedManagedPolicy] | None = None
    CreateDate: StrictStr | None = None
    GroupId: StrictStr | None = None
    GroupName: StrictStr | None = None
    GroupPolicyList: list[SecurityHubAwsIamGroupPolicy] | None = None
    Path: StrictStr | None = None
