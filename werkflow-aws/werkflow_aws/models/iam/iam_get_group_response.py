from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .iam_group import IAMGroup
from .iam_user import IAMUser


class IAMGetGroupResponse(BaseModel):
    Group: IAMGroup | None = None
    Users: list[IAMUser] | None = None
    IsTruncated: StrictBool | None = None
    Marker: StrictStr | None = None
