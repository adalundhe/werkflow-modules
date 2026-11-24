from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .storage_gateway_vtl_device import StorageGatewayVTLDevice


class StorageGatewayDescribeVTLDevicesResponse(BaseModel):
    GatewayARN: StrictStr | None = None
    VTLDevices: list[StorageGatewayVTLDevice] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
