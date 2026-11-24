from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .storage_gateway_bandwidth_rate_limit_interval import StorageGatewayBandwidthRateLimitInterval


class StorageGatewayDescribeBandwidthRateLimitScheduleResponse(BaseModel):
    GatewayARN: StrictStr | None = None
    BandwidthRateLimitIntervals: list[StorageGatewayBandwidthRateLimitInterval] | None = None
    ResponseMetadata: dict[str, Any] | None = None
