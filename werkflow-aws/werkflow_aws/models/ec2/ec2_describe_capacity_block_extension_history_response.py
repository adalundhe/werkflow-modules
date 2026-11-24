from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_capacity_block_extension import EC2CapacityBlockExtension


class EC2DescribeCapacityBlockExtensionHistoryResponse(BaseModel):
    CapacityBlockExtensions: list[EC2CapacityBlockExtension] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
