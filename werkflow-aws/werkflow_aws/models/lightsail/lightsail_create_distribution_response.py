from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lightsail_distribution import LightsailDistribution
from .lightsail_operation import LightsailOperation


class LightsailCreateDistributionResponse(BaseModel):
    distribution: LightsailDistribution | None = None
    operation: LightsailOperation | None = None
    ResponseMetadata: dict[str, Any] | None = None
