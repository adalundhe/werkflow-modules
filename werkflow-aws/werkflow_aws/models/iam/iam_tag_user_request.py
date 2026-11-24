from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .iam_tag_model import IAMTagModel


class IAMTagUserRequest(BaseModel):
    UserName: StrictStr
    Tags: list[IAMTagModel]
