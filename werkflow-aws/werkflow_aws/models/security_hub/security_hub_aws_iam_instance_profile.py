from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_iam_instance_profile_role import SecurityHubAwsIamInstanceProfileRole


class SecurityHubAwsIamInstanceProfile(BaseModel):
    Arn: StrictStr | None = None
    CreateDate: StrictStr | None = None
    InstanceProfileId: StrictStr | None = None
    InstanceProfileName: StrictStr | None = None
    Path: StrictStr | None = None
    Roles: list[SecurityHubAwsIamInstanceProfileRole] | None = None
