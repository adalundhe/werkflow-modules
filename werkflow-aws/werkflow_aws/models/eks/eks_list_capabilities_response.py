from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .eks_capability_summary import EKSCapabilitySummary


class EKSListCapabilitiesResponse(BaseModel):
    capabilities: list[EKSCapabilitySummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
