from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .storage_gateway_gateway_info import StorageGatewayGatewayInfo


class StorageGatewayListGatewaysResponse(BaseModel):
    Gateways: list[StorageGatewayGatewayInfo] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
