from __future__ import annotations
from pydantic import BaseModel
from .iam_group import IAMGroup


class IAMCreateGroupResponse(BaseModel):
    Group: IAMGroup | None = None
