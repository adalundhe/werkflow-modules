from __future__ import annotations
from pydantic import BaseModel
from .iam_policy_version import IAMPolicyVersion


class IAMGetPolicyVersionResponse(BaseModel):
    PolicyVersion: IAMPolicyVersion | None = None
