from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .iam_attached_permissions_boundary_model import IAMAttachedPermissionsBoundaryModel
from .iam_tag_model import IAMTagModel


class IAMUserModel(BaseModel):
    Path: StrictStr | None = None
    UserName: StrictStr | None = None
    UserId: StrictStr | None = None
    Arn: StrictStr | None = None
    CreateDate: datetime.datetime | StrictStr | None = None
    PasswordLastUsed: datetime.datetime | StrictStr | None = None
    PermissionsBoundary: IAMAttachedPermissionsBoundaryModel | None = None
    Tags: list[IAMTagModel] | None = None
