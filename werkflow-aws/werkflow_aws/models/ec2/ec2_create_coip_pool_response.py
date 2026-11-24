from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_coip_pool import EC2CoipPool


class EC2CreateCoipPoolResponse(BaseModel):
    CoipPool: EC2CoipPool | None = None
    ResponseMetadata: dict[str, Any] | None = None
