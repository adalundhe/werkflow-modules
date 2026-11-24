from __future__ import annotations
from pydantic import BaseModel
from .iam_policy import IAMPolicy


class IAMGetPolicyResponse(BaseModel):
    Policy: IAMPolicy | None = None
