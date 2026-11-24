from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .iam_tag import IAMTag


class IAMCreateRoleRequest(BaseModel):
    RoleName: StrictStr
    AssumeRolePolicyDocument: StrictStr
    Path: StrictStr | None = None
    Description: StrictStr | None = None
    MaxSessionDuration: StrictInt | None = None
    MaxSigninSessionDuration: StrictInt | None = None
    PermissionsBoundary: StrictStr | None = None
    Tags: list[IAMTag] | None = None
