from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .iam_group import IAMGroup


class IAMListGroupsResponse(BaseModel):
    Groups: list[IAMGroup] | None = None
    IsTruncated: StrictBool | None = None
    Marker: StrictStr | None = None
