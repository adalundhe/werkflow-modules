from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .iam_role_model import IAMRoleModel
from .iam_tag_model import IAMTagModel


class IAMInstanceProfileModel(BaseModel):
    Path: StrictStr | None = None
    InstanceProfileName: StrictStr | None = None
    InstanceProfileId: StrictStr | None = None
    Arn: StrictStr | None = None
    CreateDate: datetime.datetime | StrictStr | None = None
    Roles: list[IAMRoleModel] | None = None
    Tags: list[IAMTagModel] | None = None
