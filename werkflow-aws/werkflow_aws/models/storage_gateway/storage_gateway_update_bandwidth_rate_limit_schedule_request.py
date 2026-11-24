from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .storage_gateway_bandwidth_rate_limit_interval import StorageGatewayBandwidthRateLimitInterval


class StorageGatewayUpdateBandwidthRateLimitScheduleRequest(BaseModel):
    GatewayARN: StrictStr
    BandwidthRateLimitIntervals: list[StorageGatewayBandwidthRateLimitInterval]
