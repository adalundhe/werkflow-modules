from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .organizations_resource_policy import OrganizationsResourcePolicy


class OrganizationsPutResourcePolicyResponse(BaseModel):
    ResourcePolicy: OrganizationsResourcePolicy | None = None
    ResponseMetadata: dict[str, Any] | None = None
