from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .iam_password_policy import IAMPasswordPolicy


class IAMGetAccountPasswordPolicyResponse(BaseModel):
    PasswordPolicy: IAMPasswordPolicy | None = None
    ResponseMetadata: dict[str, Any] | None = None
