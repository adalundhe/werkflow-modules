from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsIamInstanceProfileRole(BaseModel):
    Arn: StrictStr | None = None
    AssumeRolePolicyDocument: StrictStr | None = None
    CreateDate: StrictStr | None = None
    Path: StrictStr | None = None
    RoleId: StrictStr | None = None
    RoleName: StrictStr | None = None
