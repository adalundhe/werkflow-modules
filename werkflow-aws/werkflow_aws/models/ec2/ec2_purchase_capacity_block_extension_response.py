from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_capacity_block_extension import EC2CapacityBlockExtension


class EC2PurchaseCapacityBlockExtensionResponse(BaseModel):
    CapacityBlockExtensions: list[EC2CapacityBlockExtension] | None = None
    ResponseMetadata: dict[str, Any] | None = None
