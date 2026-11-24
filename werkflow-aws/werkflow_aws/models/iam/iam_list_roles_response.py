from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .iam_role import IAMRole


class IAMListRolesResponse(BaseModel):
    Roles: list[IAMRole] | None = None
    IsTruncated: StrictBool | None = None
    Marker: StrictStr | None = None
