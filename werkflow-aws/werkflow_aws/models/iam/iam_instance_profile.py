from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .iam_role import IAMRole
from .iam_tag import IAMTag


class IAMInstanceProfile(BaseModel):
    Path: StrictStr | None = None
    InstanceProfileName: StrictStr | None = None
    InstanceProfileId: StrictStr | None = None
    Arn: StrictStr | None = None
    CreateDate: datetime.datetime | None = None
    Roles: list[IAMRole] | None = None
    Tags: list[IAMTag] | None = None
