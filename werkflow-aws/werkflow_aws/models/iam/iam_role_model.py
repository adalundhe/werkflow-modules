from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .iam_attached_permissions_boundary_model import IAMAttachedPermissionsBoundaryModel
from .iam_role_last_used_model import IAMRoleLastUsedModel
from .iam_source_role_template_model import IAMSourceRoleTemplateModel
from .iam_tag_model import IAMTagModel


class IAMRoleModel(BaseModel):
    Path: StrictStr | None = None
    RoleName: StrictStr | None = None
    RoleId: StrictStr | None = None
    Arn: StrictStr | None = None
    CreateDate: datetime.datetime | StrictStr | None = None
    AssumeRolePolicyDocument: StrictStr | None = None
    Description: StrictStr | None = None
    MaxSessionDuration: StrictInt | None = None
    MaxSigninSessionDuration: StrictInt | None = None
    PermissionsBoundary: IAMAttachedPermissionsBoundaryModel | None = None
    Tags: list[IAMTagModel] | None = None
    RoleLastUsed: IAMRoleLastUsedModel | None = None
    SourceRoleTemplate: IAMSourceRoleTemplateModel | None = None
