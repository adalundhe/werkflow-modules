from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .iam_role_model import IAMRoleModel


class IAMUpdateRoleDescriptionResponse(BaseModel):
    Role: IAMRoleModel | None = None
    ResponseMetadata: dict[str, Any] | None = None
