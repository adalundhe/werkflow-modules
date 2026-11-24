from __future__ import annotations
from pydantic import BaseModel
from .iam_user import IAMUser


class IAMGetUserResponse(BaseModel):
    User: IAMUser | None = None
