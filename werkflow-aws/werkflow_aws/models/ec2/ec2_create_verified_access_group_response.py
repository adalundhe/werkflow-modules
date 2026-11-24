from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_verified_access_group import EC2VerifiedAccessGroup


class EC2CreateVerifiedAccessGroupResponse(BaseModel):
    VerifiedAccessGroup: EC2VerifiedAccessGroup | None = None
    ResponseMetadata: dict[str, Any] | None = None
