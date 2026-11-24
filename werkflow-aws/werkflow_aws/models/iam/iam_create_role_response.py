from __future__ import annotations
from pydantic import BaseModel
from .iam_role import IAMRole


class IAMCreateRoleResponse(BaseModel):
    Role: IAMRole | None = None
