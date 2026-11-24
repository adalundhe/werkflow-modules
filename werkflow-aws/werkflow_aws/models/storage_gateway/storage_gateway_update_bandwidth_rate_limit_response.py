from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class StorageGatewayUpdateBandwidthRateLimitResponse(BaseModel):
    GatewayARN: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
