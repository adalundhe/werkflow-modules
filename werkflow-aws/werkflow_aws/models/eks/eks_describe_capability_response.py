from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .eks_capability import EKSCapability


class EKSDescribeCapabilityResponse(BaseModel):
    capability: EKSCapability | None = None
    ResponseMetadata: dict[str, Any] | None = None
