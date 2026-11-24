from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .security_hub_aws_iam_policy_version import SecurityHubAwsIamPolicyVersion


class SecurityHubAwsIamPolicyDetails(BaseModel):
    AttachmentCount: StrictInt | None = None
    CreateDate: StrictStr | None = None
    DefaultVersionId: StrictStr | None = None
    Description: StrictStr | None = None
    IsAttachable: StrictBool | None = None
    Path: StrictStr | None = None
    PermissionsBoundaryUsageCount: StrictInt | None = None
    PolicyId: StrictStr | None = None
    PolicyName: StrictStr | None = None
    PolicyVersionList: list[SecurityHubAwsIamPolicyVersion] | None = None
    UpdateDate: StrictStr | None = None
