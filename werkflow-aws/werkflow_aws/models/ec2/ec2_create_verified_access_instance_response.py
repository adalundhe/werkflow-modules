from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_verified_access_instance import EC2VerifiedAccessInstance


class EC2CreateVerifiedAccessInstanceResponse(BaseModel):
    VerifiedAccessInstance: EC2VerifiedAccessInstance | None = None
    ResponseMetadata: dict[str, Any] | None = None
