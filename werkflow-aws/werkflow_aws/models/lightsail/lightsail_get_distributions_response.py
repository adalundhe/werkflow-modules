from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lightsail_distribution import LightsailDistribution


class LightsailGetDistributionsResponse(BaseModel):
    distributions: list[LightsailDistribution] | None = None
    nextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
