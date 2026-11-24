from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .iam_user import IAMUser


class IAMListUsersResponse(BaseModel):
    Users: list[IAMUser] | None = None
    IsTruncated: StrictBool | None = None
    Marker: StrictStr | None = None
