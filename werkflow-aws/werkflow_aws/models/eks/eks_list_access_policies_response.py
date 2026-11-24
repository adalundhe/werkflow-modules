from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .eks_access_policy import EKSAccessPolicy


class EKSListAccessPoliciesResponse(BaseModel):
    accessPolicies: list[EKSAccessPolicy] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
