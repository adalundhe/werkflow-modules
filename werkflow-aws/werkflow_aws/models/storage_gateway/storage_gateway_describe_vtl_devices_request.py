from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class StorageGatewayDescribeVTLDevicesRequest(BaseModel):
    GatewayARN: StrictStr
    VTLDeviceARNs: list[StrictStr] | None = None
    Marker: StrictStr | None = None
    Limit: StrictInt | None = None
