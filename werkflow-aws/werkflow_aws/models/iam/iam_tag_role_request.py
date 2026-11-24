from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .iam_tag_model import IAMTagModel


class IAMTagRoleRequest(BaseModel):
    RoleName: StrictStr
    Tags: list[IAMTagModel]
