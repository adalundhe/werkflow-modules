from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .iam_attached_permissions_boundary import IAMAttachedPermissionsBoundary
from .iam_role_last_used import IAMRoleLastUsed
from .iam_source_role_template import IAMSourceRoleTemplate
from .iam_tag import IAMTag


class IAMRole(BaseModel):
    Path: StrictStr | None = None
    RoleName: StrictStr | None = None
    RoleId: StrictStr | None = None
    Arn: StrictStr | None = None
    CreateDate: datetime.datetime | None = None
    AssumeRolePolicyDocument: StrictStr | None = None
    Description: StrictStr | None = None
    MaxSessionDuration: StrictInt | None = None
    MaxSigninSessionDuration: StrictInt | None = None
    PermissionsBoundary: IAMAttachedPermissionsBoundary | None = None
    Tags: list[IAMTag] | None = None
    RoleLastUsed: IAMRoleLastUsed | None = None
    SourceRoleTemplate: IAMSourceRoleTemplate | None = None
