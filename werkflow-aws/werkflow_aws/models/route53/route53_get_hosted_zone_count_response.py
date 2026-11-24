from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt


class Route53GetHostedZoneCountResponse(BaseModel):
    HostedZoneCount: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
