from __future__ import annotations
from pydantic import BaseModel
from .iam_role import IAMRole


class IAMGetRoleResponse(BaseModel):
    Role: IAMRole | None = None
