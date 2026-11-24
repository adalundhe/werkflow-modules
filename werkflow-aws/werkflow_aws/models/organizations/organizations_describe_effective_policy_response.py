from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .organizations_effective_policy import OrganizationsEffectivePolicy


class OrganizationsDescribeEffectivePolicyResponse(BaseModel):
    EffectivePolicy: OrganizationsEffectivePolicy | None = None
    ResponseMetadata: dict[str, Any] | None = None
