from __future__ import annotations
from pydantic import BaseModel
from .organizations_policy import OrganizationsPolicy


class OrganizationsDescribePolicyResponse(BaseModel):
    Policy: OrganizationsPolicy | None = None
