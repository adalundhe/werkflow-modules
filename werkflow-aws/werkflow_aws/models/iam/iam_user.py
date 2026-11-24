from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .iam_attached_permissions_boundary import IAMAttachedPermissionsBoundary
from .iam_tag import IAMTag


class IAMUser(BaseModel):
    Path: StrictStr | None = None
    UserName: StrictStr | None = None
    UserId: StrictStr | None = None
    Arn: StrictStr | None = None
    CreateDate: datetime.datetime | None = None
    PasswordLastUsed: datetime.datetime | None = None
    PermissionsBoundary: IAMAttachedPermissionsBoundary | None = None
    Tags: list[IAMTag] | None = None
