from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .organizations_policy_model import OrganizationsPolicyModel


class OrganizationsCreatePolicyResponse(BaseModel):
    Policy: OrganizationsPolicyModel | None = None
    ResponseMetadata: dict[str, Any] | None = None
