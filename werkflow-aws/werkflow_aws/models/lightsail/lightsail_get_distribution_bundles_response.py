from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lightsail_distribution_bundle import LightsailDistributionBundle


class LightsailGetDistributionBundlesResponse(BaseModel):
    bundles: list[LightsailDistributionBundle] | None = None
    ResponseMetadata: dict[str, Any] | None = None
