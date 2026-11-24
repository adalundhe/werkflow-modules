from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .storage_gateway_pool_info import StorageGatewayPoolInfo


class StorageGatewayListTapePoolsResponse(BaseModel):
    PoolInfos: list[StorageGatewayPoolInfo] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
