from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .iam_group_model import IAMGroupModel


class IAMListGroupsForUserResponse(BaseModel):
    Groups: list[IAMGroupModel] | None = None
    IsTruncated: StrictBool | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
