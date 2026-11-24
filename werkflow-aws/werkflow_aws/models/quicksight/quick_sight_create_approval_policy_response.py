from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .quick_sight_approval_policy import QuickSightApprovalPolicy


class QuickSightCreateApprovalPolicyResponse(BaseModel):
    Policy: QuickSightApprovalPolicy | None = None
    ResponseMetadata: dict[str, Any] | None = None
