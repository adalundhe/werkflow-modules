from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_region import EC2Region


class EC2DescribeRegionsResponse(BaseModel):
    Regions: list[EC2Region] | None = None
    ResponseMetadata: dict[str, Any] | None = None
